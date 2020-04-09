#!/bin/bash
# This script takes an URL, sends a request and displays the size of the body of
curl -sI "$1" | grep Content-Length | cut --delimiter " " -f2
