#!/bin/bash

# Exit on fail
set -e

# Ensure all gems installed. Add binstubs to bin which has been added to PATH in Dockerfile.
bundle check || bundle install --binstubs="$BUNDLE_BIN"
exec "$@"
