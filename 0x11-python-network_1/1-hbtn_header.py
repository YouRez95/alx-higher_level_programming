#!/usr/bin/python3
import sys
from urllib import request
"""
  module to send a request and get X-Request-Id header
"""


url = sys.argv[1]
with request.urlopen(url) as response:
    print(response.getheader('X-Request-Id'))
