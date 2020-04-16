#!/usr/bin/python3
import requests
import sys

if __name__ == '__main__':
    r = requests.put(sys.argv[1])
    if r.status_code <= 399:
        print(r.text)
    else:
        print("Error code: {}".format(r.status_code))
