FROM ruby:2.5.1 as base

ARG APP_DIR=/usr/src/app
ARG AWS_ACCESS_KEY_ID=''
ARG AWS_DEFAULT_REGION=us-west-2
ARG AWS_SECRET_ACCESS_KEY=''
ARG BUNDLE_PATH=/bundle
ARG BUNDLE_BIN=/bundle/bin
ARG GEM_HOME=/usr/local/bundle
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
	LANG=${LANG}

ENV PATH="${BUNDLE_BIN}:${PATH}"

# Ensure that our apt package list is updated and install a few
# packages to ensure that we can compile assets (nodejs).
RUN 		apt-get update \
			&& apt-get install -qq -y --no-install-recommends \
  				build-essential

# Add app files into docker image
COPY 		* ${APP_DIR}/

WORKDIR 	${APP_DIR}
RUN 		chmod +x entrypoint.sh \
			&& chmod +x run_bot.rb \
			&& chmod +x gunny.rb \
			&& chmod +x web_recon.rb

ENTRYPOINT ["./entrypoint.sh"]
CMD ["bundle"]

FROM alpine:latest

ARG APP_DIR=/usr/src/app
ARG AWS_ACCESS_KEY_ID=''
ARG AWS_DEFAULT_REGION=us-west-2
ARG AWS_SECRET_ACCESS_KEY=''
ARG BUNDLE_PATH=/bundle
ARG BUNDLE_BIN=/bundle/bin
ARG GEM_HOME=/usr/local/bundle
ARG LANG=C.UTF-8
ARG LOG_DIR=/usr/src/app/logs
ARG LOG_PATH=/usr/src/app/logs/log
ARG QUEUE_URL=''
ARG SELENIUM_HOST=0.0.0.0
ARG SELENIUM_PORT=4444

COPY --from=base  	${APP_DIR} 		${APP_DIR}/
COPY --from=base 	${BUNDLE_BIN} 	${BUNDLE_BIN}/
COPY --from=base 	${RUBY} 		${RUBY}/
COPY --from=base 	${GEM_HOME} 	${GEM_HOME}/

ENV APP_DIR=${APP_DIR} \
	AWS_ACCESS_KEY_ID=${AWS_ACCESS_KEY_ID} \
	AWS_DEFAULT_REGION=${AWS_DEFAULT_REGION} \
	AWS_SECRET_ACCESS_KEY=${AWS_SECRET_ACCESS_KEY} \
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

WORKDIR 	${APP_DIR}
# ENTRYPOINT ["./entrypoint.sh"]
# CMD ["ruby", "run_bot.rb"]
ENTRYPOINT  ["ruby", "run_bot.rb"]
