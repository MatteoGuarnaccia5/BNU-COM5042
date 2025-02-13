#!/bin/sh

kubectl apply --kustomize kubernetes/prod/
kubectl rollout restart deploy/smart-home-app -n apps

echo "Deployed production"