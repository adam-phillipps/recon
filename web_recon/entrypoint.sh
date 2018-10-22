#!/bin/bash

# Exit on fail
set -e

# Pass commands through docker to process
exec "$@"
