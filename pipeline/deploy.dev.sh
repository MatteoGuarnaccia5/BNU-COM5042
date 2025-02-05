#!/bin/sh

kubectl apply --kustomize kubernetes/dev/
kubectl rollout restart deploy/smart-home-app -n apps