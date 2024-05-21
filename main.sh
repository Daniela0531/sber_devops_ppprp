##!/bin/sh
# deployment, conteyner, чтобы снаружи было доступно - service
# bin bash
# docker create image приложения
# docker create image скрипта
#
# create deployment через манифест/кубстл
#
# для app create service
#
# pod-forward
#
# теперь надо создать крон job
#
# в job запустить скрипт
# нужно указать volumes (один из 3-х), лучше персистентное либо host pass
eval $(minikube docker-env)

cd app/
docker build -t app:latest .

cd ../deployment
kubectl apply -f app.yaml

cd ../do_requests
docker build -t do_request:latest .

cd ../deployment
kubectl apply -f request.yaml