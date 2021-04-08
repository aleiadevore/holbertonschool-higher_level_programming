#!/bin/bash
# Displays all methods
curl -siX OPTIONS "$1" | grep "Allow:" | cut -d " " -f2-
