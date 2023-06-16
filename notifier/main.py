from cloudevents.http import from_http
from flask import Flask, jsonify, request

application = Flask(__name__)


@application.route('/status')
def status():
    return jsonify({'status': 'ok'})


@application.route('/', methods=['POST'])
def log():
    event = from_http(request.headers, request.get_data())

    if event.data['legitimacy'] != 'legitimate':
        # fake call to notification service
        print("Calling notification service")
        print(f"Received event: {event}")

    return "", 200
