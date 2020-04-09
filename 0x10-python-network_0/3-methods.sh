#!/usr/bin/env bash
# This script takes an URL, sends a request and displays the methods the server.
curl -sIX OPTIONS "$1" | grep Allow | cut --delimiter ":" -f2 | awk '$1=$1'
