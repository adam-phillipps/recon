#!/bin/bash

# Exit on fail
set -e

# install package dependencies
python $APP_DIR/setup.py install

# allow commands to pass through entrypoint from docker run
# commands
exec "$@"