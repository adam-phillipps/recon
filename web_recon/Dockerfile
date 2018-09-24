FROM ruby:2.5.1

ARG APP_DIR=/usr/src/app
ARG BUNDLE_PATH=/bundle
ARG BUNDLE_BIN=/bundle/bin
ARG GEM_HOME=/bundle
ARG LANG=C.UTF-8
ARG LOG_DIR=/usr/src/app/logs
ARG LOG_PATH=/usr/src/app/logs/log
ARG QUEUE_URL=''
ARG SELENIUM_HOST=0.0.0.0
ARG SELENIUM_PORT=4444

# Give bots the location of the queue that holds the jobs.
# Bundle installs with binstubs to our custom /bundle/bin volume path
# Let system use those stubs.
ENV APP_DIR=${APP_DIR} \
	BUNDLE_PATH=${BUNDLE_PATH} \
    BUNDLE_BIN=${BUNDLE_BIN} \
    GEM_HOME=${GEM_HOME} \
	LANG=${LANG} \
	LOG_DIR=${LOG_DIR} \
	LOG_PATH=${LOG_PATH} \
	QUEUE_URL=${QUEUE_URL} \
	SELENIUM_PORT=${SELENIUM_PORT} \
	SELENIUM_HOST=${SELENIUM_HOST}

ENV PATH="${BUNDLE_BIN}:${PATH}"

# Ensure that our apt package list is updated and install a few
# packages to ensure that we can compile assets (nodejs).
RUN 		apt-get update \
			&& apt-get install -qq -y --no-install-recommends \
  				build-essential

# Add app files into docker image
WORKDIR 	${APP_DIR}
COPY 		* ${APP_DIR}/

RUN 		chmod +x entrypoint.sh

ENTRYPOINT ["./entrypoint.sh"]
#CMD ["/bin/bash"]
CMD ["ruby", "run_bot.rb"]
