FROM conda/miniconda3-centos7

ARG APP_DIR=/usr/src/app
ENV APP_DIR=${APP_DIR}

RUN mkdir -p ${APP_DIR}

COPY ./* ${APP_DIR}

WORKDIR ${APP_DIR}

RUN pip install --upgrade pip \
	&& pip install gensim

EXECUTE ["./entrypoint"]
CMD ["python", "from_redshift.py", "query.sql"]
