#!/bin/bash
# Displays all methods
curl -sIX OPTIONS "$1" | grep "Allow:" | cut -d " " -f2-
