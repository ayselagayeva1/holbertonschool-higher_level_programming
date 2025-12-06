#!/usr/bin/python3
"""
Sends a letter as POST parameter 'q' to http://0.0.0.0:5000/search_user
and displays the result if valid JSON is returned.
"""

import sys
import requests


if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    q = sys.argv[1] if len(sys.argv) > 1 else ""

    try:
        response = requests.post(url, data={"q": q})
        try:
            result = response.json()
        except ValueError:
            print("Not a valid JSON")
        else:
            if result:
                print(f"[{result.get('id')}] {result.get('name')}")
            else:
                print("No result")
    except requests.RequestException:
        print("No result")
