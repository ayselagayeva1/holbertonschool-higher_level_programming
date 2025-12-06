#!/usr/bin/python3
"""
Takes GitHub credentials (username and personal access token) and
displays the user's id using the GitHub API.
"""

import sys
import requests


if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]  # personal access token

    url = "https://api.github.com/user"

    try:
        response = requests.get(url, auth=(username, token))
        if response.status_code == 200:
            user_data = response.json()
            print(user_data.get("id"))
        else:
            print(None)
    except requests.RequestException:
        print(None)
