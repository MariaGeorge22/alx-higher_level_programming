#!/usr/bin/python3
"""
Module
"""
import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]
    with requests.get(url) as response:
        body = response.text
        if response.status_code >= 400:
            print("Error code: {}".format(response.status_code))
        else:
            print(body)
