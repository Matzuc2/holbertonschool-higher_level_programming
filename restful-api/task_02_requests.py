#!/usr/bin/python3
import requests
import csv

"""
This module provides functions to fetch posts from an API,
print them, and save them to a CSV file.

Functions:
    - fetch_and_print_posts(): Fetches posts from an API
    and prints their titles.
    - fetch_and_save_posts(): Fetches posts from an API and saves
      selected fields to a CSV file.
"""


"""r = requests.get('https://jsonplaceholder.typicode.com/posts')
response = r.json()
print(response)"""


def fetch_and_print_posts():
    """
    Fetches posts from the JSONPlaceholder API and prints their titles.

    The function makes a GET request to retrieve all posts from the API.
    It then iterates over the response and prints the title of each post.

    Returns:
        None
    """
    r = requests.get('https://jsonplaceholder.typicode.com/posts')
    print("Status code:", r.status_code)
    response = r.json()
    for i in response:
        print(i["title"])


def fetch_and_save_posts():
    """
    Fetches posts from the JSONPlaceholder API and
    saves selected fields to a CSV file.

    The function makes a GET request to retrieve all posts.
    It filters each post to keep only 'id', 'title', and 'body'.
    The filtered data is then written to 'posts.csv' using the csv module.

    Returns:
        None
    """
    list1 = []
    dict1 = {}
    r = requests.get('https://jsonplaceholder.typicode.com/posts')
    response = r.json()
    for i in response:
        dict1 = i.copy()
        for k in list(dict1.keys()):
            if k != 'id' and k != 'body' and k != 'title':
                del dict1[k]
        list1.append(dict1)
    with open('posts.csv', 'w', newline='') as csvfile:
        csv_writer =\
            csv.DictWriter(csvfile, fieldnames=['id', 'title', 'body'])
        csv_writer.writeheader()
        csv_writer.writerows(list1)


"""
Alternative Implementation:

This version constructs a filtered dictionary directly
instead of modifying a copy.

def fetch_and_save_posts():
    '''
    Fetches posts from the JSONPlaceholder API and saves
      selected fields to a CSV file.

    This implementation directly extracts only 'id',
      'title', and 'body' fields.
    The filtered data is written to 'posts.csv' using the csv module.

    Returns:
        None
    '''
    list1 = []
    r = requests.get('https://jsonplaceholder.typicode.com/posts')
    response = r.json()

    for i in response:
        dict1 = {
            'id': i['id'],
            'title': i['title'],
            'body': i['body']
        }
        list1.append(dict1))
    with open('posts.csv', 'w', newline='') as csvfile:
        csv_writer =\
            csv.DictWriter(csvfile, fieldnames=['id', 'title', 'body'])
        csv_writer.writeheader()
        csv_writer.writerows(list1)
"""
