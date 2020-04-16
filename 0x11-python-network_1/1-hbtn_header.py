#!/usr/bin/python3
import urllib.request
import sys

with urllib.request.urlopen(sys.argv[1]) as response:
    html = response.info()
    print(html['X-Request-Id'])
