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


### Services
For each app in the system, we create a deployment/service/etc.  Kubernetes will get a `Deployment` object, ECS will get a `AWS::ECS::Service` resource and so on.  These services do different things and they're all required but they don't need to be running at the same time; They just need to run _at some point_.

The different services are:
- JobLoader
	- example -> takes data from somewhere, like a sql query against Redshift, and converts it into a row per message in a queue.
- PageSim
	- Document similarities Modeling project to yield fewer but more accurate results to another higher level model that needs many good comparison documents.
- WebRecon
	- Another Distributed, RPC, dynamic, topic and command generalized crawl/scrapper to gather documents from the web which require some unique per page navigation; e.g. Amazon document for Armagedon DVD vs Best Buy Armagedon DVD.  Both are required candidate documents and both have unique paths to arrive at them.  This project can go get both of these via machine created RPC jobs in a queue without having a URL to use or originate from.
	https://smile.amazon.com/Armageddon-Bruce-Willis/dp/B00000G3PA/ref=smi_www_rco2_go_smi_g1405964225?_encoding=UTF8&%2AVersion%2A=1&%2Aentries%2A=0&ie=UTF8
	and
	https://www.bestbuy.com/site/armageddon-dvd-1998/3549609.p?skuId=3549609&ref=212&loc=1&gclid=CjwKCAjwo_HdBRBjEiwAiPPXpCJtxaprK2hLgW9AnAN3rxM4auAr_zRDWy2D4T2FssVnJxNw7fM1BhoCXqUQAvD_BwE&gclsrc=aw.ds


## TODO:
- Create kubernetes deployments for the `job_loader` and `pagesim` apps
- Improve corpus.
	- The current corpus is a Wikipedia dump.  The Recon app needs to be set to
	work against several different domains or someone needs to tell me how to google better data sets...The PageSims model will suck until it gets good documents to compare to and Wikipedia isn't so good for everything.
- Improve the README.....
- Contemplate harder on switching from Capybara to Twisted for the WebRecon project.
- Create better kube orchestration
- Create Cloud resource templates (Like Cloudformation for EC2s for a cluster, etc)
	- AWS:
		- SQS queue, nothing special
		- N number of EC2s, let's start with one or two
		- S3 bucket for artifacts like the corpora and the model(s)
