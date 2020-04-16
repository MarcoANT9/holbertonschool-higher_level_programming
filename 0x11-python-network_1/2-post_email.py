#!/usr/bin/python3
"""This script takes two arguments, the first one is the ip direction to send
   the request and the second is the email to send.                       """
import urllib.request
import urllib.parse
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    value = {'email': argv[1]}
    data = urllib.parse.urlencode(value)
    data = data.encode("utf-8")
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        print(response.read().decode("utf-8"))
