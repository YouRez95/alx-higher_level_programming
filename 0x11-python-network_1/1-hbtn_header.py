#!/usr/bin/python3
import sys
import urllib
"""
  module to send a request and get X-Request-Id header
"""


url = sys.argv[1]
with urllib.request.urlopen(url) as response:
    print(response.getheader('X-Request-Id'))
