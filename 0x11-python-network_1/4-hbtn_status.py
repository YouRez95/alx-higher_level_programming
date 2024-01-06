#!/usr/bin/python3
"""
  module to send a request and get response
"""


import requests

r = requests.get('https://alx-intranet.hbtn.io/status')
print('Body response:')
print('\t- type: {}'.format(type(r.text)))
print('\t- content: {}'.format(r.text))
