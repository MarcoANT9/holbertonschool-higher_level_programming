#!/usr/bin/python3
"""This script takes two arguments, the first one is the ip direction to send
   the request and the second is the email to send.                       """
import urllib.request
import urllib.parse
import sys

if __name__ == '__main__':

    data = {'email': sys.argv[2]}
    url = sys.argv[1]
    post = urllib.parse.urlencode(data).encode('utf-8')
    req = urllib.request.Request(url, post)
    with urllib.request.urlopen(req) as response:
        email = response.read()
        print(email)
