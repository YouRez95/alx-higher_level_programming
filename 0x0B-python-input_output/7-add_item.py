#!/usr/bin/python3
""" module """


from sys import argv
from os import path
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file


file_name = "add_item.json"
data = []
if not path.exists(file_name):
    save_to_json_file(data, file_name)

if len(argv) > 1:
    data = load_from_json_file(file_name)
    for i in range(1, len(argv)):
        data.append(argv[i])
    save_to_json_file(data, file_name)
