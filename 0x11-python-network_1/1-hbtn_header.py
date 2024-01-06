#!/usr/bin/python3
import sys
import urllib.request
"""
  module to send a request and get X-Request-Id header
"""


if __name__ == "__main__":
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        print(response.getheader('X-Request-Id'))
