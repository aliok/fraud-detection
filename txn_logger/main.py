from cloudevents.http import from_http
from flask import Flask, jsonify, request
from prometheus_client import Counter
from prometheus_client import start_http_server

application = Flask(__name__)

txn_counter = Counter('transactions', 'Transactions', ['legitimacy', 'amount'])


@application.route('/status')
def status():
    return jsonify({'status': 'ok'})


@application.route('/', methods=['POST'])
def log():
    event = from_http(request.headers, request.get_data())

    print(f"Received event: {event}")

    legitimacy = event.data['legitimacy']
    amount = event.data["amount"]

    txn_counter.labels(legitimacy=legitimacy, amount=amount).inc()

    return "", 200


# start prometheus server
start_http_server(8000)
