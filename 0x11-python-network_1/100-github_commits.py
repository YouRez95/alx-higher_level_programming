#!/usr/bin/python3
"""
  module to send a request and get response
"""


import sys
import requests

if __name__ == "__main__":
    repo_name = sys.argv[1]
    owner_name = sys.argv[2]

    url = "https://api.github.com/repos/{}/{}/commits".format(
        owner_name, repo_name)
    headers = {'Accept': 'application/vnd.github+json',
               'X-GitHub-Api-Version': '2022-11-28'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        response = response.json()
        for i in range(10):
            print("{}: {}".format(response[i]['sha'],
                                  response[i]['commit']['author']['name']))
