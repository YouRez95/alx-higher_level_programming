#!/usr/bin/python3
"""
  module to send a request and get X-Request-Id header
"""

import sys
import urllib.request
import urllib.error

if __name__ == "__main__":
    req = urllib.request.Request(sys.argv[1])
    try:
        with urllib.request.urlopen(req) as response:
            data = response.read()
            print(data.decode("UTF-8"))
    except urllib.error.HTTPError as e:
        print('Error code: {}'.format(e.code))
