import json
import random

from flask import Flask, jsonify, request
from cloudevents.http import CloudEvent
from cloudevents.conversion import to_binary
import requests
import os

BROKER_URL = os.environ.get('BROKER_URL')
POD_NAME = os.environ.get('POD_NAME')

application = Flask(__name__)


@application.route('/')
@application.route('/status')
def status():
    return jsonify({'status': 'ok'})


@application.route('/pos', methods=['POST'])
def pos():
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
    # 1/4 of the time, we'll send a short interarrival time
    if random.random() < 0.25:
        data["interarrival"] = random.randint(1, 25)
    else:
        data["interarrival"] = random.randint(1000, 1000000)

    # 1/4 of the time, we'll mark it as foreign
    if random.random() < 0.25:
        data["foreign"] = "True"
    else:
        data["foreign"] = "False"

    event = CloudEvent(attributes, data)
    headers, body = to_binary(event)
    requests.post(BROKER_URL, data=body, headers=headers)

    return "", 200
