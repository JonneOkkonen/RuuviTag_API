import flask
from flask import request, jsonify

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


@app.errorhandler(404)
def page_not_found(e):
    response = [
        {
            "status": "error",
            "message": "The resource could not be found."
        }
    ]
    return jsonify(response), 404

app.run()