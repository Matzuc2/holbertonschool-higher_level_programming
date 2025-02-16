#!/usr/bin/python3

"""
This module provides functions for serializing and deserializing
 Python dictionaries using XML.

Functions:
    - serialize_to_xml(dictionary, filename): Converts a
    dictionary to an XML file.
    - deserialize_from_xml(filename): Reads an XML file
      and reconstructs the dictionary.
"""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serializes a dictionary into an XML file.

    Args:
        dictionary (dict): The dictionary to be serialized.
        filename (str): The name of the output XML file.

    Returns:
        None
    """
    root = ET.Element("data")

    for key, value in dictionary.items():
        child = ET.Element(key)
        child.text = str(value)
        root.append(child)

    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=True)


def deserialize_from_xml(filename):
    """
    Deserializes an XML file into a Python dictionary.

    Args:
        filename (str): The name of the XML file to be deserialized.

    Returns:
        dict: A dictionary containing the deserialized data.
    """
    tree = ET.parse(filename)
    root = tree.getroot()

    return {child.tag: child.text for child in root}
