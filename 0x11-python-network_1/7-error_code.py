#!/usr/bin/python3
"""
  module to send a request and get response
"""


import sys
import requests

if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    code = r.status_code
    if code >= 400:
        print('Error code: {}'.format(code))
    else:
        print(r.text)
