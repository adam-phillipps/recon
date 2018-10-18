#!/bin/bash

# Exit on fail
set -e

# install package dependencies
python /usr/src/app/setup.py install

# allow commands to pass through entrypoint from docker run
# commands
exec "$@"