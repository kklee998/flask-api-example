# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 17:31:02 2018

@author: Keifer
"""
import requests
import pandas as pd
from datetime import datetime


def get_launch(mode="verbose", sort_="asc", next_=50,
                    limit=3000, id_=0, name_=None, locationid=None,
                    rocketid=None, lsp=None, startdate_="1900-01-01",
                    enddate_="2018-10-19"):

    url = "https://launchlibrary.net/1.4/launch/"

    payload_past = {"mode": mode, "limit": limit, "startdate": startdate_,
                    "enddate": enddate_}
    payload_future = {"mode": mode, "limit": limit, "next": limit}

    data_past = requests.get(url, params=payload_past).json()
    data_future = requests.get(url, params=payload_future).json()

    return [data_past, data_future]


def get_canaveral_data(raw_data):

    # Canaveral params declaration
    canaveral_id = []
    canaveral_status = []
    canaveral_lsp = []
    canaveral_narration = []
    canaveral_vehicle = []

    # Non-Canaveral params decalaration
    others_id = []
    others_status = []
    others_lsp = []
    others_narration = []
    others_vehicle = []

    for item in raw_data:

        # Grab Canaveral launches only
        if item['location']['id'] == 16:

            canaveral_id.append(item)
            canaveral_status.append(item['status'])
            canaveral_vehicle.append(item['rocket'])

            if item['missions']:
                canaveral_narration.append(item['missions'][0])
            else:
                canaveral_narration.append([])

            try:
                canaveral_lsp.append(item['lsp'])
            except:
                if item['rocket']['agencies']:
                    canaveral_lsp.append(item['rocket']['agencies'][0])
                else:
                    canaveral_lsp.append([])

        else:
            others_id.append(item)
            others_status.append(item['status'])
            others_vehicle.append(item['rocket'])

            if item['missions']:
                others_narration.append(item['missions'][0])
            else:
                others_narration.append([])

            try:
                others_lsp.append(item['lsp'])
            except:
                if item['rocket']['agencies']:
                    others_lsp.append(item['rocket']['agencies'][0])
                else:
                    others_lsp.append([])

    # Temp holder
    canaveral_data = [canaveral_id, canaveral_status, canaveral_lsp, canaveral_narration,
                      canaveral_vehicle]
    others_data = [others_id, others_status,
        others_lsp, others_narration, others_vehicle]

    return canaveral_data, others_data


if __name__ == "__main__":

    # Getting launch data
    general_launch = get_launch()

    """---------------------------------------------------------------------"""
    # Getting past data
    past_launch = general_launch[0]['launches']
    past_canaveral, past_others = get_canaveral_data(past_launch)

    # Getting future data
    future_launch = general_launch[1]['launches']
    future_canaveral, future_others = get_canaveral_data(future_launch)

    # Rocket Info Canaveral
    pcr = past_canaveral[4]
    pcr_name = []

    for item in pcr:

        # If it's unique
        if item['name'] not in pcr_name:
            pcr_name.append(item['name'])

        else:
            pass

    """---------------------------------------------------------------------"""
    # Hardcoding rocket info
    rocket_info = {'Atlas LV-3B': {'height': 25, 'diameter': 3.05, 'mass': 117730,
                                   'payload capacity': 1360, 'success': 7, 'failures': 2,
                                   'retired': 1, 'cost': 14210000},
                   'Titan II GLV': {'height': 33.2, 'diameter': 3.05, 'mass': 154200,
                                   'payload capacity': 3580, 'success': 12, 'failures': 0,
                                   'retired': 1, 'cost': 0},
                   'Titan IIIE': {'height': 48.8, 'diameter': 3.05, 'mass': 632970,
                                   'payload capacity': 15400, 'success': 6, 'failures': 1,
                                   'retired': 1, 'cost': 322000000},
                   'Titan IVB': {'height': 62, 'diameter': 3.05, 'mass': 943050,
                                   'payload capacity': 21680, 'success': 15, 'failures': 2,
                                   'retired': 1, 'cost': 432000000,
                   'Delta IV Heavy': {'height': 72, 'diameter': 5, 'mass': 733000,
                                   'payload capacity': 28790, 'success': 9, 'failures': 1,
                                   'retired': 1, 'cost': 322000000,
                   'Falcon 9 v1.2': {'height': 71, 'diameter': 3.66, 'mass': 549054,
                                   'payload capacity': 22800, 'success': 40, 'failures': 40,
                                   'retired': 0, 'cost': 5000000}
