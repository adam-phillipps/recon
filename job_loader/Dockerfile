# WIP as pseudo-code
from python:alpine

COPY ./* ${APP_DIR}

EXECUTE ["./entrypoint"]
CMD ["python", "-m", "from_redshift.handler", "pdp_as_row.sql"]
