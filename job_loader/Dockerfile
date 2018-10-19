FROM frolvlad/alpine-miniconda3

ARG APP_DIR=/usr/src/app
ARG AWS_DEFAULT_REGION=us-west-2
ARG BACKLOG=''
ARG DBHOST=''
ARG DBPASS=''
ARG DBUSER=''
ARG DBNAME=''

ENV APP_DIR=${APP_DIR} \
	AWS_DEFAULT_REGION=${AWS_DEFAULT_REGION} \
	BACKLOG=${BACKLOG} \
	DBHOST=${DBHOST} \
	DBPASS=${DBPASS} \
	DBUSER=${DBUSER} \
	DBNAME=${DBNAME}

WORKDIR ${APP_DIR}
RUN 	mkdir -p ${APP_DIR}/job_loader
COPY 	environment.yml ${APP_DIR}
RUN 	conda env create -f=environment.yml -n job_loader \
		&& echo "source activate job_loader" >> ~/.bashrc

# Create app directories
COPY 	./ ${APP_DIR}/

# Make entrypoint runable and install build dependencies
RUN 	chmod +x ${APP_DIR}/job_loader/entrypoint.sh \
		&& chmod +x ${APP_DIR}/job_loader/row_to_job.py

# Run 'er
WORKDIR 	${APP_DIR}/job_loader
ENTRYPOINT 	["./entrypoint.sh"]
CMD 		["python", "row_to_job.py"]
