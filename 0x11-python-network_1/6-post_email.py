#!/usr/bin/python3
"""
Module
"""
import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]
    body = {
        'email': sys.argv[2]
    }
    with requests.post(url, data=body) as response:
        body = response.text
        print(body)
