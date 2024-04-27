#!/usr/bin/python3
"""
Module
"""
import sys
import requests

if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    q = ""
    if len(sys.argv) > 1:
        q = sys.argv[1]
    body = {
        'q': q
    }
    with requests.post(url, data=body) as response:
        try:
            body = response.json()
            if not body:
                print("No result")
            else:
                print(f"[{body.get('id')}] {body.get('name')}")
        except ValueError:
            print("Not a valid JSON")
