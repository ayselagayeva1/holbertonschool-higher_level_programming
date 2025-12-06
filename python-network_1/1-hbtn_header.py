#!/usr/bin/python3
"""
Sends a request to a URL and displays the value of the
X-Request-Id variable found in the header of the response.
"""

import sys
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]

    with urllib.request.urlopen(url) as response:
        request_id = response.headers.get("X-Request-Id")

    print(request_id)
