#!/bin/bash

set -x

kubectl apply -f config/000-broker.yaml
kubectl wait broker default --for=condition=Ready --timeout=300s

kubectl apply -f config/100-pos.yaml
kubectl wait pod point-of-sales --for=condition=ContainersReady --timeout=300s

kubectl apply -f config/200-detector.yaml
kubectl wait pod fraud-detector --for=condition=ContainersReady --timeout=300s
kubectl wait trigger fraud-detector --for=condition=Ready --timeout=300s

kubectl apply -f config/300-txn-logger.yaml
kubectl wait pod transaction-logger --for=condition=ContainersReady --timeout=300s
kubectl wait trigger transaction-logger --for=condition=Ready --timeout=300s

kubectl apply -f config/400-notifier.yaml
kubectl wait pod notifier --for=condition=ContainersReady --timeout=300s
kubectl wait trigger notifier --for=condition=Ready --timeout=300s

kubectl apply -f config/900-prometheus.yaml
kubectl wait deployment prometheus-deployment --for=condition=Available --timeout=300s

kubectl apply -f config/901-grafana.yaml
kubectl wait deployment grafana --for=condition=Available --timeout=300s

kubectl apply -f config/999-event-generator.yaml
kubectl wait containersource event-generator --for=condition=Ready --timeout=300s
