#!/usr/bin/python3
"""
  module to send a request and get some info
"""


from urllib import request

with request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    peek = response.peek()
    data = response.read()
    utf_content = data.decode('UTF-8')
    print('Body response:')
    print('    - type: {}'.format(type(data)))
    print('    - content: {}'.format(peek))
    print('    - utf8 content: {}'.format(utf_content))
