# WIP as pseudo-code
from python:alpine

COPY ./* ${APP_DIR}

ARG BACKLOG_QUEUE
ARG DBHOST
ARG DBPASS
ARG DBUSER
ARG DBNAME

ENV BACKLOG_QUEUE=${BACKLOG_QUEUE} \
	DBHOST=${DBHOST} \
	DBPASS=${DBPASS} \
	DBUSER=${DBUSER} \
	DBNAME=${DBNAME}

EXECUTE ["./entrypoint"]
CMD ["python", "from_redshift.py"]
