# Recon project

## Description
These codes can take directions from a message and do things that are
suited to a distributed workflow.

## Local Setup
- install `minikube`
- install `kubectl`

		$ brew cask install minikube
		$ brew install kubernetes-cli
		$ git clone <this repo>
		$ minikube start
		$ kubectl create -f deployments.yaml
		$ kubectl expose <kubectl get deployments result>

or in pure docker, using `docker-compose` commands.
