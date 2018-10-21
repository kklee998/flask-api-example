import requests


def pad(pad_id):
    url = "https://launchlibrary.net/1.4/pad?id=" + pad_id
    r = requests.get(url)

    return r.json()


def location():
    url = "https://launchlibrary.net/1.4/location/USA"
    r = requests.get(url).json()

    return r


def mission():
    url = "https://launchlibrary.net/1.4/launch/1059"
    r = requests.get(url).json()

    return r


def mission_summary():
    url = "https://launchlibrary.net/1.4/mission/552?mode=summary"
    return requests.get(url).json()


def mission_payload():

    url = "https://launchlibrary.net/1.4/mission/552"
    data = requests.get(url).json()
    mission = data['missions']
    payloads = []
    for item in mission:
        payloads.append(item['payloads'])
    return payloads


def upcoming_launch():
    url = "https://launchlibrary.net/1.4/launch/2018-10-21?locationid=164"
    r = requests.get(url).json()

    return r


def past_launch():
    url = "https://launchlibrary.net/1.4/launch?locationid=164"
    r = requests.get(url).json()

    return r


def launch_name():
    url = "https://launchlibrary.net/1.4/launch/1059?fields=name"
    r = requests.get(url).json()

    return r


def vehicle_name():
    url = "https://launchlibrary.net/1.4/rocket/8"
    return requests.get(url).json()


def launch_summary():
    url = "https://launchlibrary.net/1.4/launch/1059?mode=summary"
    return requests.get(url).json()


def rocket_info():
    url = "https://launchlibrary.net/1.4/rocket/8"
    return requests.get(url).json()
