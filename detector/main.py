import json
from flask import Flask, jsonify, request
import pandas as pd
import cloudpickle as cp
from cloudevents.http import from_http
from cloudevents.conversion import to_structured
import os

POD_NAME = os.environ.get('POD_NAME')
application = Flask(__name__)
pipeline = cp.load(open('pipeline.pkl', 'rb'))


def predict(args_dict):
    d = {'timestamp': 0, 'label': 0, 'user_id': args_dict.get('user_id'), 'amount': args_dict.get('amount'),
         'merchant_id': args_dict.get('merchant_id'), 'trans_type': args_dict.get('trans_type'),
         'foreign': args_dict.get('foreign'), 'interarrival': args_dict.get('interarrival')}
    df = pd.DataFrame(d, index=[0])
    return pipeline.predict(df)[0]


@application.route('/status')
def status():
    return jsonify({'status': 'ok'})


@application.route('/', methods=['POST'])
def detect():
    event = from_http(request.headers, request.get_data())
    print(
        f"Found {event['id']} from {event['source']} with type "
        f"{event['type']} and specversion {event['specversion']}"
    )

    data = request.data or '{}'
    body = json.loads(data)
    prediction = predict(body)

    event.data['legitimacy'] = prediction

    event['type'] = 'com.example.transaction.checked'
    event['source'] = POD_NAME

    headers, body = to_structured(event)

    return body, 200, headers

# if __name__ == '__main__':
#
#     #
#
#     my_req = {"user_id": 1698,
#               "amount": 7915,
#               "merchant_id": 22.37,
#               "trans_type": "contactless",
#               "foreign": "False",
#               "interarrival": 9609}
#     r1 = predict(my_req)
#     print(r1)
#     # {'prediction': 'legitimate'}
#
#     other_req = {"user_id": 9999,
#                  "amount": 100,
#                  "merchant_id": 99999,
#                  "trans_type": "online",
#                  "foreign": "False",
#                  "interarrival": 100}
#     r2 = predict(other_req)
#     print(r2)
#     # {'prediction': 'fraud'}
