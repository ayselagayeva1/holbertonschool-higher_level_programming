#!/usr/bin/python3
"""
Task 02 - Working with the requests library and JSONPlaceholder API
"""

import requests
import csv


API_URL = "https://jsonplaceholder.typicode.com/posts"


def fetch_and_print_posts():
    """
    Fetches all posts from JSONPlaceholder and prints the status code
    and the title of each post if successful.
    """
    response = requests.get(API_URL)

    # Print the status code
    print(f"Status Code: {response.status_code}")

    # If request is successful
    if response.status_code == 200:
        data = response.json()  # Parse JSON

        # Print all titles
        for post in data:
            print(post.get("title"))
    else:
        print("Failed to fetch posts.")


def fetch_and_save_posts():
    """
    Fetches all posts from JSONPlaceholder and saves them to posts.csv
    with id, title, and body fields.
    """
    response = requests.get(API_URL)

    if response.status_code == 200:
        data = response.json()

        # Build a list of dictionaries containing only needed fields
        formatted_posts = [
            {
                "id": post.get("id"),
                "title": post.get("title"),
                "body": post.get("body")
            }
            for post in data
        ]

        # Write data to CSV
        with open("posts.csv", "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=["id", "title", "body"])
            writer.writeheader()
            writer.writerows(formatted_posts)

        print("posts.csv successfully created.")
    else:
        print("Failed to fetch posts.")
