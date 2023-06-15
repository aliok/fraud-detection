import json
import time

from flask import Flask, jsonify, request
from cloudevents.http import CloudEvent
from cloudevents.conversion import to_binary
import requests
import os

BROKER_URL = os.environ.get('BROKER_URL')
POD_NAME = os.environ.get('POD_NAME')

application = Flask(__name__)

# map <merchant_id, datetime>
TxnTimes = {}


@application.route('/')
@application.route('/status')
def status():
    return jsonify({'status': 'ok'})


@application.route('/pos', methods=['POST'])
def create_prediction():
    data = request.data or '{}'
    body = json.loads(data)

    attributes = {
        "type": "transaction.created",
        "source": POD_NAME,
    }
    data = {
        "user_id": body["user_id"],
        "amount": body["amount"],
        "merchant_id": body["merchant_id"],
        "trans_type": body["trans_type"],
    }
    now = time.time_ns() // 1_000_000
    if body["merchant_id"] in TxnTimes:
        data["interarrival"] = now - TxnTimes[body["merchant_id"]]
    else:
        data["interarrival"] = 10000000
    TxnTimes[body["merchant_id"]] = now

    if int(body["merchant_id"]) % 2 == 0:
        data["foreign"] = "True"
    else:
        data["foreign"] = "False"

    event = CloudEvent(attributes, data)
    headers, body = to_binary(event)
    requests.post(BROKER_URL, data=body, headers=headers)

    return "", 200
