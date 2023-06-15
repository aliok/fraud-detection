#!/bin/bash

set -x

cd detector
docker build . -t aliok/fraud-detector:latest
docker push aliok/fraud-detector:latest
cd ..

cd event_generator
docker build . -t aliok/event-generator:latest
docker push aliok/event-generator:latest
cd ..



cd notifier
docker build . -t aliok/notifier:latest
docker push aliok/notifier:latest
cd ..

cd point_of_sales
docker build . -t aliok/point-of-sales:latest
docker push aliok/point-of-sales:latest
cd ..

cd txn_logger
docker build . -t aliok/transaction-logger:latest
docker push aliok/transaction-logger:latest
cd ..

