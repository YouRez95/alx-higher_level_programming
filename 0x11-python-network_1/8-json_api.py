#!/usr/bin/python3
"""
  module to send a request and get response
"""


import sys
import requests

if __name__ == "__main__":
    if len(sys.argv) > 1:
        query = {'q': sys.argv[1]}
    else:
        query = {'q': '""'}

    r = requests.post("http://localhost:5000/search_user", query)
    result = ''
    notValid = False
    try:
        result = r.json()
    except ValueError:
        print('Not a valid JSON')
        notValid = True
    if notValid is False:
        if not result:
            print('No result')
        else:
            print('[{}] {}'.format(result['id'], result['name']))
