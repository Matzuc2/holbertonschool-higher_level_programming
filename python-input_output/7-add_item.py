#!/usr/bin/python3
"""
This script adds all command-line arguments to a Python list
and saves them to a file in JSON format.

Usage:
    ./add_item.py arg1 arg2 arg3 ...

Functionality:
    - Loads an existing list from `add_item.json` (if it exists).
    - Adds all command-line arguments to the list.
    - Saves the updated list back to `add_item.json`.

Modules:
    - sys: For reading command-line arguments.
    - os.path: To check if the JSON file exists.
    - load_from_json_file: Loads a list from JSON.
    - save_to_json_file: Saves a list to JSON.
"""

import os
from sys import argv

# Import functions from previous tasks
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

file_path = "add_item.json"

# Load existing list or create a new one
if os.path.exists(file_path):
    my_list = load_from_json_file(file_path)
else:
    my_list = []

# Extend list with new command-line arguments
my_list.extend(argv[1:])

# Save updated list back to the JSON file
save_to_json_file(my_list, file_path)
