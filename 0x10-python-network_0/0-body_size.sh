#!/usr/bin/env bash
# This script takes an URL, sends a request and displays the size of the body of
# the response.
# → Arg[0] = Filename (not used)
# → Arg[1] = URL to send request.

curl -sIX POST "$1" | grep Content-Length | cut --delimiter " " -f2
