#!/usr/bin/python3
"""
Takes in a URL, sends a request to the URL and displays the body
of the response. If the status code is >= 400, prints the error code.
"""

import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]

    try:
        response = requests.get(url)
        if response.status_code >= 400:
            print(f"Error code: {response.status_code}")
        else:
            print(response.text)
    except requests.RequestException as e:
        # Genel bir network hatası olursa yakalar
        print(f"Error: {e}")
