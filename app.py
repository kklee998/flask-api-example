from flask import Flask, request, jsonify
from flask_cors import CORS
import main

app = Flask(__name__)
CORS(app)


@app.route('/')
def home():
    return "/pad"


@app.route("/pad", methods=["GET"])
def get_pad():
    if request.method == "GET":
        return (jsonify(main.pad("164")))


@app.route("/location", methods=["GET"])
def get_location():
    if request.method == "GET":
        return(jsonify(main.location()))


@app.route("/USA-mission", methods=["GET"])
def get_mission():
    if request.method == "GET":
        return(jsonify(main.mission()))


@app.route("/launch", methods=["GET"])
def get_upcoming_launch():
    if request.method == "GET":
        return(jsonify(main.upcoming_launch()))


@app.route("/launch_name", methods=["GET"])
def launch_name():
    if request.method == "GET":
        return(jsonify(main.launch_name()))


@app.route("/vehicle_name", methods=["GET"])
def vehicle_name():
    if request.method == "GET":
        return(jsonify(main.vehicle_name()))


@app.route("/past", methods=["GET"])
def get_past_launch():
    if request.method == "GET":
        return(jsonify(main.past_launch()))


@app.route("/launch_summary", methods=["GET"])
def launch_summary():
    if request.method == "GET":
        return(jsonify(main.launch_summary()))


@app.route("/rocket_info", methods=["GET"])
def rocket_info():
    if request.method == "GET":
        return(jsonify(main.rocket_info()))


@app.route("/mission_summary", methods=["GET"])
def mission_summary():
    if request.method == "GET":
        return(jsonify(main.mission_summary()))


@app.route("/mission_payload", methods=["GET"])
def mission_payload():
    if request.method == "GET":
        return(jsonify(main.mission_payload()))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
