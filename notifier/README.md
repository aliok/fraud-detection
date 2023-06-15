```shell
python3 -m pip install -r requirements.txt
```

```shell
FLASK_ENV=development FLASK_APP=main.py FLASK_RUN_PORT=9000 flask run

curl "http://127.0.0.1:9000" \
  -H 'Host: example.com' \
  -X POST \
  -H "Ce-Specversion: 1.0" \
  -H "Ce-Type: test.event" \
  -H "Ce-Source: test.source" \
  -H "Ce-time: 2020-12-02T13:49:13.77Z" \
  -H "Ce-Id: 536808d3-88be-4077-9d7a-a3f162705f79" \
  -H "Content-Type: application/json" \
  -d '{"user_id": 1698, "amount": 7915, "merchant_id": 22.37, "trans_type": "contactless", "foreign": "False", "interarrival": 9609, "legitimacy": "legitimate"}'

> HTTP/1.1 200 OK

curl "http://127.0.0.1:9000" \
  -H 'Host: example.com' \
  -X POST \
  -H "Ce-Specversion: 1.0" \
  -H "Ce-Type: test.event" \
  -H "Ce-Source: test.source" \
  -H "Ce-time: 2020-12-02T13:49:13.77Z" \
  -H "Ce-Id: 536808d3-88be-4077-9d7a-a3f162705f79" \
  -H "Content-Type: application/json" \
  -d '{"user_id": 1698, "amount": 7915, "merchant_id": 22.37, "trans_type": "contactless", "foreign": "False", "interarrival": 9609, "legitimacy": "fraud"}'
  
> HTTP/1.1 200 OK
```

```shell
docker build . -t aliok/notifier

docker run -p 9000:9000 --rm aliok/notifier
```
