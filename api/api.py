import flask
from flask import request, jsonify
import json
import multiprocessing as mp
from listener import listener

app = flask.Flask(__name__)
app.config["DEBUG"] = False

global configData
global data
configData = ""
data = mp.Manager().list()

@app.before_request
def initializeServer():
    global configData
    global data
    # Read data from config.json
    with open('config.json') as f:
        configData = json.load(f)

    # Start RuuviTag Listeners
    for tag in configData["ruuvitags"]:
        data.append("Loading... Try again soon.")
        mp.Process(target=listener, args=(data, tag, 10,)).start()

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
    global configData
    global data
    ruuvitag = ""
    # Find ruuvitag from list
    for tag in configData["ruuvitags"]:
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
        return jsonify([{
            "status": "success",
            "message": data[ruuvitag["index"]]
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

if __name__ == '__main__':
    app.run()