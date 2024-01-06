#!/usr/bin/python3
"""
  module to send a request and get response
"""


import sys
import requests

if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]

    headers = {'Authorization': 'Bearer {}'.format(
        token), 'X-GitHub-Api-Version': '2022-11-28'}
    url = "https://api.github.com/users/{}".format(username)
    response = requests.get(url, headers=headers)
    print(response.json()['id'])
