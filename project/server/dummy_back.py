import time

from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin

app = Flask(__name__)
# Signing Access-Control-Allow-Origin. This is CRITICAL.
CORS(app)

@app.route('/dummy', methods=['GET'])
def get_patient_list():
    return jsonify({ "status" : "success" })
app.run()
