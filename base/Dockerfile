FROM ruby:2.5.1

ENV LANG C.UTF-8

ARG BUNDLE_PATH=/bundle
ARG BUNDLE_BIN=/bundle/bin
ARG GEM_HOME=/bundle
ARG QUEUE_URL=''
ARG APP_DIR=/usr/src/app

# Give bots the location of the queue that holds the jobs.
# Bundle installs with binstubs to our custom /bundle/bin volume path
# Let system use those stubs.
ENV APP_DIR=${APP_DIR} \
	QUEUE_URL=${QUEUE_URL} \
	BUNDLE_PATH=${BUNDLE_PATH} \
    BUNDLE_BIN=${BUNDLE_BIN} \
    GEM_HOME=${GEM_HOME}

ENV PATH="${BUNDLE_BIN}:${PATH}"

RUN curl -sS -o - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add
RUN echo "deb [arch=amd64]  http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list

# Ensure that our apt package list is updated and install a few
# packages to ensure that we can compile assets (nodejs).
RUN apt-get update && apt-get install -qq -y --no-install-recommends \
      build-essential nodejs unzip xvfb xauth libxi6 \
      libgconf-2-4 default-jdk google-chrome-stable

RUN wget https://chromedriver.storage.googleapis.com/2.42/chromedriver_linux64.zip \
	&& unzip chromedriver_linux64.zip \
	&& mv chromedriver /usr/bin/chromedriver \
	&& chown root:root /usr/bin/chromedriver \
	&& chmod +x /usr/bin/chromedriver

# Start selenium
# RUN xvfb-run java -Dwebdriver.chrome.driver=/usr/bin/chromedriver -jar selenium-server-standalone.jar
# chromedriver --url-base=/wd/hub



# Add app files into docker image
RUN mkdir -p ${APP_DIR}
WORKDIR ${APP_DIR}
COPY * ${APP_DIR}/

# Add bundle entry point to handle bundle cache
WORKDIR ${APP_DIR}
RUN chmod +x entrypoint.sh

ENTRYPOINT ["./entrypoint.sh"]
CMD ["/bin/bash"]