#!/bin/bash

# Exit on fail
set -e

# allow commands to pass through entrypoint from docker run
# commands
exec "$@"
