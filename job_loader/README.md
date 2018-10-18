# Recon/JobLoader
This package was created to create messages in a queue out of rows from a database.  The database is currently set up as a MySQL RDBMS but it shouldn't be hard to swap that out; Just replace the dependency on mysql and include your db client instead.

## Use
You can run this package locally, in a Docker container or as a Kubernetes deployment (working on it).

### There are a few environment variables you should populate:
- `APP_DIR`	the directory from which this project will run in the container
- `BACKLOG`	the queueing system used to supply Jobs to workers
- `DBHOST`	the host that the database is running from
- `DBPASS`	the password to access the necessary tables in the db
- `DBUSER`	the user for the password you supplied, to finish satisfying login
- `DBNAME`	is the name of the RDBMS database you want to pull rows from

### Running in Docker
This will start a container locally, get records from the db, create Jobs from the rows it just received and push the Jobs up to a queue.
`docker build -t allpps/jobloader . \
	&& docker run --env-file .env -it $(docker images -qa | head -n1)`