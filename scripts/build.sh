#!/bin/bash

# Build script for MONEI Python SDK

if [ "$1" == "local" ]; then
  # Build using local OpenAPI spec
  openapi-generator-cli generate -i ./openapi.json -c ./config.json
else
  # Build using remote OpenAPI spec
  openapi-generator-cli generate -i https://js.monei.com/api/v1/openapi.json -c ./config.json
fi

# Run post-build script
./scripts/post-build.sh 