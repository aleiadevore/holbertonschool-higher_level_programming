#!/bin/bash
# Displays status code only
curl -s -o /dev/null -I -w "%{http_code}" "$1"
