```shell
python3 -m pip install -r requirements.txt
```

```shell
FLASK_ENV=development FLASK_APP=main.py FLASK_RUN_PORT=9000 flask run

curl -v "http://127.0.0.1:9000/predictions" \
  -H 'Host: example.com' \
  -X POST \
  -H "Ce-Specversion: 1.0" \
  -H "Ce-Type: test.event" \
  -H "Ce-Source: test.source" \
  -H "Ce-time: 2020-12-02T13:49:13.77Z" \
  -H "Ce-Id: 536808d3-88be-4077-9d7a-a3f162705f79" \
  -H "Content-Type: application/json" \
  -d '{"user_id": 1698, "amount": 7915, "merchant_id": 22.37, "trans_type": "contactless", "foreign": "False", "interarrival": 9609}'

> {"prediction":"legitimate"}

curl -v "http://127.0.0.1:9000/predictions" \
  -H 'Host: example.com' \
  -X POST \
  -H "Ce-Specversion: 1.0" \
  -H "Ce-Type: test.event" \
  -H "Ce-Source: test.source" \
  -H "Ce-time: 2020-12-02T13:49:13.77Z" \
  -H "Ce-Id: 536808d3-88be-4077-9d7a-a3f162705f79" \
  -H "Content-Type: application/json" \
  -d '{"user_id": 1698, "amount": 100, "merchant_id": 9999, "trans_type": "online", "foreign": "False", "interarrival": 1}'

> {"prediction":"fraud"}
```

```shell
docker build . -t aliok/fraud-detector

docker run -p 9000:9000 --rm aliok/fraud-detector

curl -v "http://127.0.0.1:9000/predictions" \
  -H 'Host: example.com' \
  -X POST \
  -H "Ce-Specversion: 1.0" \
  -H "Ce-Type: test.event" \
  -H "Ce-Source: test.source" \
  -H "Ce-time: 2020-12-02T13:49:13.77Z" \
  -H "Ce-Id: 536808d3-88be-4077-9d7a-a3f162705f79" \
  -H "Content-Type: application/json" \
  -d '{"user_id": 1698, "amount": 7915, "merchant_id": 22.37, "trans_type": "contactless", "foreign": "False", "interarrival": 9609}'

> {"prediction":"legitimate"}

> {"prediction":"legitimate"}

curl -v "http://127.0.0.1:9000/predictions" \
  -H 'Host: example.com' \
  -X POST \
  -H "Ce-Specversion: 1.0" \
  -H "Ce-Type: test.event" \
  -H "Ce-Source: test.source" \
  -H "Ce-time: 2020-12-02T13:49:13.77Z" \
  -H "Ce-Id: 536808d3-88be-4077-9d7a-a3f162705f79" \
  -H "Content-Type: application/json" \
  -d '{"user_id": 1698, "amount": 100, "merchant_id": 9999, "trans_type": "online", "foreign": "False", "interarrival": 1}'

> {"prediction":"fraud"}
```
