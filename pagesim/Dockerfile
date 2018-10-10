FROM conda/miniconda3-centos7

ARG APP_DIR=/usr/src/app
ARG CORPUS_FILE=/usr/src/app/pre/corpus

ENV APP_DIR=${APP_DIR} \
	CORPUS_FILE=${CORPUS_FILE}

RUN mkdir -p ${APP_DIR}/pre

COPY ./* ${APP_DIR}

WORKDIR ${APP_DIR}

RUN pip install --upgrade pip \
	&& pip install gensim

EXECUTE ["./entrypoint", "python", "d2v_setup.py"]
CMD ["--corpus-file", $CORPUS_FILE]
