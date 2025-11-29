#!/usr/bin/python3
"""Serialize and Deserialize dictionary to/from XML"""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serialize a Python dictionary to an XML file.

    Args:
        dictionary (dict): Dictionary to serialize
        filename (str): Filename to write XML data to
    """
    root = ET.Element("data")
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=True)


def deserialize_from_xml(filename):
    """
    Deserialize XML file back into a Python dictionary.

    Args:
        filename (str): Filename of the XML file

    Returns:
        dict: Deserialized dictionary
    """
    tree = ET.parse(filename)
    root = tree.getroot()
    result = {}
    for child in root:
        result[child.tag] = child.text
    return result
