#!/usr/bin/python3
"""
This module is a script that takes all arguments it receives
and saves them into a file; first it pass the arguments to an array and
then converts it into a json string to save in the file.
"""


import sys
save_json = __import__('7-save_to_json_file').save_to_json_file
load_json = __import__('8-load_from_json_file').load_from_json_file

argc = len(sys.argv)
arg_index = 1

my_file = "add_item.json"
try:
    arg_list = load_json(my_file)
except IOError:
    arg_list = []

while arg_index < argc:
    arg_list.append(sys.argv[arg_index])
    arg_index += 1

save_json(arg_list, my_file)
