ARG QUEUE_URL

FROM allpps/recon-base:latest as base

ENV QUEUE_URL=${QUEUE_URL} \
	APP_DIR=/app
COPY base:/bin/ruby
COPY * ${APP_DIR}/

ENTRYPOINT ["ruby", "${APP_DIR}/run_bot.rb"]