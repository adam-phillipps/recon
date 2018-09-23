ARG LANG=C.UTF-8

FROM ruby:2.5.1

ARG BUNDLE_PATH=/bundle
ARG BUNDLE_BIN=/bundle/bin
ARG GEM_HOME=/bundle
ARG QUEUE_URL=''
ARG APP_DIR=/usr/src/app
ARG LOG_DIR=${APP_DIR}/logs
ARG LOG_PATH=${LOG_DIR}/log

# Give bots the location of the queue that holds the jobs.
# Bundle installs with binstubs to our custom /bundle/bin volume path
# Let system use those stubs.
ENV APP_DIR=${APP_DIR} \
	BUNDLE_PATH=${BUNDLE_PATH} \
    BUNDLE_BIN=${BUNDLE_BIN} \
    GEM_HOME=${GEM_HOME} \
	LANG=${LANG} \
	QUEUE_URL=${QUEUE_URL}

ENV PATH="${BUNDLE_BIN}:${PATH}"

# Ensure that our apt package list is updated and install a few
# packages to ensure that we can compile assets (nodejs).
RUN 		apt-get update \
			&& apt-get install -qq -y --no-install-recommends \
  					build-essential

# Add app files into docker image
RUN 		mkdir -p ${LOG_DIR} \
			&& touch ${LOG_PATH} ${LOG_DIR}/errors ${LOG_DIR}/done
WORKDIR ${APP_DIR}
COPY 		* ${APP_DIR}/

# Add bundle entry point to handle bundle cache
WORKDIR 	${APP_DIR}
RUN 		chmod +x entrypoint.sh

ENTRYPOINT 	["./entrypont.sh"]
