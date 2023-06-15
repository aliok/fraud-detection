```shell
python3 -m pip install -r requirements.txt
```

```shell
K_SINK=https://example.com EVENT_COUNT=100 INTERVAL="0.1" python3 main.py

> Sending event 0/100: {'user_id': 162, 'amount': 7877, 'merchant_id': 134, 'trans_type': 'online', 'event_index': 0}
```

```shell
docker build . -t aliok/event-generator

docker run -p 9000:9000 -e K_SINK=https://example.com -e EVENT_COUNT=100 -e INTERVAL="0.1" --rm aliok/event-generator
```
