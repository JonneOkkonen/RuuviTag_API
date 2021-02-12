import flask
from flask import request, jsonify
import json
from ruuvitag_sensor.ruuvitag import RuuviTag

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    response = [
        {
            "status": "success",
            "message": "Welcome to RuuviTag API. Check routing documentation from GitHub."
        }
    ]
    return jsonify(response), 200

@app.route('/ruuvitag/read/<name>', methods=['GET'])
def RuuviTagRead(name):
    ruuvitag = ""
    # Read RuuviTags from config.json
    with open('config.json') as f:
        data = json.load(f)
    # Find ruuvitag from list
    for tag in data["ruuvitags"]:
        if tag["name"].lower() == name.lower():
            ruuvitag = tag
            break
    
    # Check if ruuvitag was found
    if(ruuvitag == ""):
        return jsonify([{
            "status": "error",
            "message": "RuuviTag with name (" + name + ") not found."
        }]), 404
    else:
        # Get Ruuvitag data
        # Device Bluetooth Address
        try:
            sensor = RuuviTag(ruuvitag["address"]).update()
        except ValueError:
            sensor = "RuuviTag address is not correct."
        except:
            sensor = "Error happened while trying to read RuuviTag values."
        return jsonify([{
            "status": "success",
            "message": sensor
        }]), 200

@app.errorhandler(404)
def page_not_found(e):
    response = [
        {
            "status": "error",
            "message": "The resource could not be found."
        }
    ]
    return jsonify(response), 404
    
app.run(host='192.168.1.107')