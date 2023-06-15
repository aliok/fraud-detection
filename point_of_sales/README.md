```shell
python3 -m pip install -r requirements.txt
```

```shell
POD_NAME=foo \
BROKER_URL=https://example.com \
FLASK_ENV=development FLASK_APP=main.py FLASK_RUN_PORT=9000 flask run

curl -v "http://127.0.0.1:9000/pos" \
  -d '{"user_id": 1698, "amount": 7915, "merchant_id": 22.37, "trans_type": "contactless"}' \
  --header "Content-Type: application/json"

> HTTP/1.1 200 OK
```

```shell
docker build . -t aliok/point-of-sales

docker run -p 9000:9000  -e POD_NAME='foo' -e BROKER_URL='https://example.com' --rm aliok/point-of-sales

curl -v "http://127.0.0.1:9000/pos" \
  -d '{"user_id": 1698, "amount": 7915, "merchant_id": 22.37, "trans_type": "contactless"}' \
  --header "Content-Type: application/json"

> HTTP/1.1 200 OK
```
