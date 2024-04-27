#!/bin/bash
# takes in a URL, sends a GET request to the URL, and stores the body and status code in an array
curl -sL -H "X-School-User-Id: 98" "$1"
