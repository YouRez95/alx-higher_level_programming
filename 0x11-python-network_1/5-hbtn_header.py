#!/usr/bin/python3
"""
  module to send a request and get header
"""


import sys
import requests

if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    print(r.headers.get('X-Request-Id'))
