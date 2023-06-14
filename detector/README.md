```shell
python3 -m pip install -r requirements.txt
```

```shell
FLASK_ENV=development FLASK_APP=main.py FLASK_RUN_PORT=9000 flask run

curl http://127.0.0.1:9000/predictions --data '{"user_id": 1698, "amount": 7915, "merchant_id": 22.37, "trans_type": "contactless", "foreign": "False", "interarrival": 9609}' --header "Content-Type: application/json"

> {"prediction":"legitimate"}

curl http://127.0.0.1:9000/predictions --data '{"user_id": 1698, "amount": 100, "merchant_id": 9999, "trans_type": "online", "foreign": "False", "interarrival": 1}' --header "Content-Type: application/json"

> {"prediction":"fraud"}
```

```shell
docker build . -t aliok/fraud-detector

docker run -p 9000:9000 --rm aliok/fraud-detector

curl http://127.0.0.1:9000/predictions --data '{"user_id": 1698, "amount": 7915, "merchant_id": 22.37, "trans_type": "contactless", "foreign": "False", "interarrival": 9609}' --header "Content-Type: application/json"

> {"prediction":"legitimate"}

curl http://127.0.0.1:9000/predictions --data '{"user_id": 1698, "amount": 100, "merchant_id": 9999, "trans_type": "online", "foreign": "False", "interarrival": 1}' --header "Content-Type: application/json"

> {"prediction":"fraud"}
```
