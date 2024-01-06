#!/usr/bin/python3
from urllib import request
"""
  module to send a request and get some info
"""


with request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    html = response.read()
    print('Body response:')
    print('      - type: {}'.format(type(html)))  # class bytes
    print('      - content: {}'.format(html))  # b'OK'
    print('      - utf8 content: {}'.format(response.msg))  # OK
