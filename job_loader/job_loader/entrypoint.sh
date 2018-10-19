#!/bin/sh
set -e

# allow commands to pass through entrypoint from docker run
# commands
source ~/.bashrc
exec "$@"
