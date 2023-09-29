#!/usr/bin/python3
"""Python script that fetches https://alx-intranet.hbtn.io/status
"""


if __name__ == "__main__":
    import requests

    url = 'https://alx-intranet.hbtn.io/status'

    req = requests.get(url)

    print("Body response:")
    print(f"\t- type: {type(req)}")
    print(f"\t- content: {req.reason}")
