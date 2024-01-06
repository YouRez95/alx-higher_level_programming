#!/usr/bin/python3
"""
  module to send a request and get response
"""


import sys
import requests

if __name__ == "__main__":
    if sys.argv[1]:
        query = {'q': sys.argv[1]}
    else:
        query = {'q': ""}

    r = requests.post("http://0.0.0.0:5000/search_user", query)
    try:
        result = r.json()
    except ValueError:
        print('Not a valid JSON')
    if result is []:
        print('No result')
    else:
        print('[{}] {}'.format(result['id'], result['name']))
