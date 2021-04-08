#!/bin/bash
# This won't work
curl -i "$1" | grep "Allow:" | awk '{ print substr($0, index($0,$2)) }'
