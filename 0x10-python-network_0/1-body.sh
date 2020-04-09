#!/usr/bin/env bash
# This script takes an URL, sends a request and displays the size of the body of
curl -sLX GET "$1"
