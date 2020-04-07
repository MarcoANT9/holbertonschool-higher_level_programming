#!/usr/bin/env bash
# This script takes an URL, sends a request to delete.
# → Arg[0] = Filename (not used)
# → Arg[1] = URL to send request.

curl -sX DELETE "$1"
