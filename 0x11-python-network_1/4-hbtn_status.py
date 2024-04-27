#!/usr/bin/python3
"""
Module
"""
import requests

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    with requests.get(url) as response:
        body = response.text
        print("Body response:")
        print(f"\t- type: {type(body)}")
        print(f"\t- content: {body}")
