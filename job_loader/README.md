# Recon/JobLoader
This package was created to create messages in a queue out of rows from a database.  The database is currently set up as a MySQL RDBMS but it shouldn't be hard to swap that out; Just replace the dependency on mysql and include your db client instead.

## Layout of the project
The tree looks a bit like this:

	~/code/recon $ tree -L 3
	├── README.md
	├── Dockerfile # Docker
	├── deployment.yaml # Kubernetes
	├── environment.yml # Conda
	├── job_loader
	│   ├── __init__.py
	│   ├── entrypoint.sh
	│   ├── query.sql
	│   └── row_to_job.py
	└── setup.py # Pip

## Use
You can run this package locally, in a Docker container or as a Kubernetes deployment (working on it).

### Setup
There are a few environment variables you should populate:
- `APP_DIR`	the directory from which this project will run in the container
- `BACKLOG`	the queueing system used to supply Jobs to workers
- `DBHOST`	the host that the database is running from
- `DBPASS`	the password to access the necessary tables in the db
- `DBUSER`	the user for the password you supplied, to finish satisfying login
- `DBNAME`	is the name of the RDBMS database you want to pull rows from
- `AWS_DEFAULT_REGION` some AWS config for you
- if you are using keys instead of role based permissions, you should also use the other AWS config items
	- `AWS_ACCESS_KEY_ID`
	- `AWS_SECRET_ACCESS_KEY`

You'll need somewhere to deploy this stuff so either Docker and Kubernetes are the preferred methods and you can also run this on a server or VM.  If you're running on a VM, there aren't _too_ many dependencies but some of them might get annoying on a VM or your local machine because they'll include C, Fortran or whatever other dependency the included libraries use.

### Running in Docker
This will start a container locally, get records from the db, create Jobs from the rows it just received and push the Jobs up to a queue.
`docker build -t allpps/job_loader . \
	&& docker run --env-file .env -it $(docker images -qa | head -n1)`

### Running in Kubernetes
The Dockerfiles will be deployed to create Pods in a Deployment for whichever service you are attempting to deploy.  None of the services require any of the other services to be running but they do require the artifacts the other services create or modify.  This means you can deploy a few JobLoaders to process a big query and after a long Halloween vacation you can come back and run the WebRecon cluster which will use the Jobs that the JobLoader created before you left.

### Notes
- Right now the JobLoader is using Conda and it works great but it might be a bit overkill and boot times can be cut down by going back to python:alpine, if possible
