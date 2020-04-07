#!/usr/bin/env bash
# This script takes an URL, sends a GET request and displays the body of the.
# response with variable "X-HolbertonSchool-User-Id"
# → Arg[0] = Filename (not used)
# → Arg[1] = URL to send request.

curl -sX GET -H "X-HolbertonSchool-User-Id" "$1"
