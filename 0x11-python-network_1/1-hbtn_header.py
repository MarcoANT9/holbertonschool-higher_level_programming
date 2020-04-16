#!/usr/bin/python3
""" This script takes a url and prints its X-Request-Id"""
import urllib.request
import sys

with urllib.request.urlopen(sys.argv[1]) as response:
    html = response.info()
    print(html['X-Request-Id'])
