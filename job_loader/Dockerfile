# WIP as pseudo-code
from python:alpine

ARG APP_DIR=/usr/src/app
ARG BACKLOG=''
ARG DBHOST=''
ARG DBPASS=''
ARG DBUSER=''
ARG DBNAME=''

ENV APP_DIR=${APP_DIR} \
	BACKLOG=${BACKLOG} \
	DBHOST=${DBHOST} \
	DBPASS=${DBPASS} \
	DBUSER=${DBUSER} \
	DBNAME=${DBNAME}

RUN mkdir -p ${APP_DIR}/job_loader
COPY ./ ${APP_DIR}/
RUN chmod +x ${APP_DIR}/entrypoint.sh

WORKDIR ${APP_DIR}
ENTRYPOINT ["/bin/sh", "./entrypoint.sh"]
CMD ["/bin/sh"]
#CMD ["python", "job_loader/from_redshift.py"]
