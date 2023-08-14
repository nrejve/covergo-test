CLUSTER_NAME := covergo-test
KUBECONFIG := $(shell kind get kubeconfig-path --name=${CLUSTER_NAME})

.PHONY: up deploy down

up:
	kind create cluster --name=${CLUSTER_NAME} --config=kind-config.yaml

deploy:
	kubectl apply -f /path/to/your/manifests

down:
	kind delete cluster --name=${CLUSTER_NAME}

