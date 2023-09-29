#!/usr/bin/python3
"""Python script that fetches https://alx-intranet.hbtn.io/status
"""


if __name__ == "__main__":
    import requests

    url = 'https://alx-intranet.hbtn.io/status'

    req = requests.get(url)

    if req.status_code >= 400:
        print(f"Error code: {req.status_code}")
    else:
        print(req.text)
