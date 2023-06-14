import json
from flask import Flask, jsonify, request
import pandas as pd
import cloudpickle as cp

application = Flask(__name__)
pipeline = cp.load(open('pipeline.pkl', 'rb'))


def predict(args_dict):
    d = {'timestamp': 0, 'label': 0, 'user_id': args_dict.get('user_id'), 'amount': args_dict.get('amount'),
         'merchant_id': args_dict.get('merchant_id'), 'trans_type': args_dict.get('trans_type'),
         'foreign': args_dict.get('foreign'), 'interarrival': args_dict.get('interarrival')}
    df = pd.DataFrame(d, index=[0])
    prediction = pipeline.predict(df)[0]
    return {'prediction': prediction}


@application.route('/')
@application.route('/status')
def status():
    return jsonify({'status': 'ok'})


@application.route('/predictions', methods=['POST'])
def create_prediction():
    data = request.data or '{}'
    body = json.loads(data)
    return jsonify(predict(body))


# if __name__ == '__main__':
#     # 'online', 'contactless', 'chip_and_pin', 'manual', 'swipe'
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
