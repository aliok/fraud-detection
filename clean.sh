#!/bin/bash

set -x

kubectl delete -f config/999-event-generator.yaml --force
kubectl delete -f config/901-grafana.yaml --force
kubectl delete -f config/900-prometheus.yaml --force
kubectl delete -f config/400-notifier.yaml --force
kubectl delete -f config/300-txn-logger.yaml --force
kubectl delete -f config/200-detector.yaml --force
kubectl delete -f config/100-pos.yaml --force
kubectl delete -f config/000-broker.yaml --force
