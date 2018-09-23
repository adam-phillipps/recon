ARG QUEUE_URL=${QUEUE_URL}
ARG APP_DIR=/usr/src/app

FROM allpps/recon-base:latest as base

ENV QUEUE_URL=${QUEUE_URL} \
	APP_DIR=${APP_DIR}

COPY * ${APP_DIR}/

WORKDIR ${APP_DIR}

ENTRYPOINT ["./entrypoint.sh"]
#CMD ["ruby", "run_bot.rb"]
CMD ["/bin/bash"]
