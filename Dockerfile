ARG QUEUE_URL

FROM allpps/web-recon

ENV QUEUE_URL=${QUEUE_URL}

ENTRYPOINT ['ruby', "${APP_DIR}/run_bot.rb"]
