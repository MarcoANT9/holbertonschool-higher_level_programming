#!/bin/bash
# This script takes an URL, sends a GET request and displays the body 
curl -sX GET -H "X-HolbertonSchool-User-Id" "$1"
