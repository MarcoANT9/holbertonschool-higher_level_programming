#!/usr/bin/python3
import requests
import sys

if __name__ == '__main__':
    payload = {'email': sysargv[2]}
    r = requests.put(sys.argv[1], data=payload)
    print("Your email is: {}".format(r.text['email']))
