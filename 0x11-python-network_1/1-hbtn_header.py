#!/usr/bin/python3
import urllib.request
import sys

req = urllib.request.Request(sys.argv[1])
with urllib.request.urlopen(req) as response:
    html = response.info()
    print(html['X-Request-Id'])
