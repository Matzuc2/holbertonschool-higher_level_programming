#!/usr/bin/python3
"""
This module provides a function to convert a CSV file into a JSON file.

The function reads data from a CSV file, converts it into a
list of dictionaries,
and then writes the JSON-formatted data to a file named 'data.json'.
It also includes basic error handling for missing files and
unexpected errors.
"""

import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Converts a CSV file into a JSON file.

    The function reads data from the specified CSV file, where each row is
    treated as a dictionary with column headers as keys. The data is then
    serialized into a JSON format and written to 'data.json'.

    Args:
        csv_filename (str): The name of the CSV file to be converted.

    Returns:
        bool: True if the conversion is successful, False if an error occurs.

    Errors:
        - If the CSV file does not exist, an error message is printed.
        - If any other unexpected exception occurs, it is caught and printed.
    """
    try:
        with open(csv_filename, 'r', encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file)
            data = list(reader)

        with open("data.json", 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4)

        return True

    except FileNotFoundError:
        print(f"Error: The file {csv_filename} was not found.")
        return False

    except Exception as e:
        print(f"An error occurred: {e}")
        return False
