#!/usr/bin/python3
"""
  module to send a request and get some info
"""


from urllib import request

if __name__ == "__main__":
    with request.urlopen('https://alx-intranet.hbtn.io/status') as response:
        peek = response.peek()
        data = response.read()
        utf_content = data.decode('UTF-8')
        print('Body response:')
        print('\t- type: {}'.format(type(data)))
        print('\t- content: {}'.format(peek))
        print('\t- utf8 content: {}'.format(utf_content))
