#!/bin/bash
# This won't work
curl -siX OPTIONS "$1" | grep "Allow:" | awk '{ print substr($0, index($0,$2)) }'
