#!/usr/bin/python3
"""
Python script that fetches https://alx-intranet.hbtn.io/status
"""
from urllib import request, response

url = 'https://alx-intranet.hbtn.io/status'

req = request.Request(url)

with request.urlopen(req) as response:
    body = response.read()

print("Body response:")
print("\t- type: {}".format(type(body)))
print("\t- content: {}".format(body))
print("\t- utf8 content: {}".format(body.decode('utf-8')))
