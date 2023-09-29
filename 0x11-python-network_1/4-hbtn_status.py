#!/usr/bin/python3
"""sends a POST request to the passed URL
"""


if __name__ == "__main__":
    import requests

    url = 'https://alx-intranet.hbtn.io/status'

    req = requests.get(url)

    print("Body response:")
    print(f"\t- type: {type(req.text)}")
    print(f"\t- content: {req.text}")
