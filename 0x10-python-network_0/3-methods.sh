#!/usr/bin/env bash
# This script takes an URL, sends a request and displays the methods the server.
# will accept.
# → Arg[0] = Filename (not used)
# → Arg[1] = URL to send request.

curl -sIX OPTIONS "$1" | grep Allow | cut --delimiter ":" -f2 | awk '$1=$1'
