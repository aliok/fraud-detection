import os
import random
import signal
import sys
import time

import requests

SINK = os.environ.get('K_SINK')
EVENT_COUNT = os.environ.get('EVENT_COUNT', 1000)
INTERVAL = os.environ.get('INTERVAL', 0.1)

headers = {'Content-type': 'application/json'}

if __name__ == "__main__":
    def signal_handler(sig, frame):
        print('Stopping')
        sys.exit(0)


    signal.signal(signal.SIGINT, signal_handler)

    print(f"Sending {EVENT_COUNT} events to {SINK} with interval {INTERVAL}")

    for i in range(int(EVENT_COUNT)):
        body = {
            "user_id": random.randint(1, 1000),
            "amount": random.choice([100, 7877, 2234, 56345, 9996]),
            "merchant_id": random.randint(1, 1000),
            "trans_type": random.choice(['online', 'contactless', 'chip_and_pin', 'manual', 'swipe']),
            "event_index": i,
        }
        print(f"Sending event {i}/{int(EVENT_COUNT)}: {body}")
        requests.post(SINK, json=body, headers=headers)
        time.sleep(float(INTERVAL))

    while True:
        time.sleep(1)
