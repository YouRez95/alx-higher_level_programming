#!/usr/bin/python3
"""
  module to send a request and get response
"""


import requests

r = requests.get('https://alx-intranet.hbtn.io/status')
print('Body response:')
print('    - type: {}'.format(type(r.text)))
print('    - content: {}'.format(r.text))
