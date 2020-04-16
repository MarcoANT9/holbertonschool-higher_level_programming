#!/usr/bin/python3
"""This script takes two arguments, the first one is the ip direction to send
   the request and the second is the email to send.                       """
import urllib.request
import urllib.parse
from sys import argv

if __name__ == "__main__":
    req = urllib.request.Request(argv[1])
    try:
        with urllib.request.urlopen(req) as response:
            print(response.read())
    except urllib.error.HTTPError as error:
        print("Error code: {}".format(error.code))
