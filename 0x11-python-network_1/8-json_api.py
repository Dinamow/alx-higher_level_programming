#!/usr/bin/python3
"""Python script that fetches https://alx-intranet.hbtn.io/status
"""


def search_user(letter):
    import requests

    url = "http://0.0.0.0:5000/search_user"
    params = {'q': letter}
    response = requests.post(url, params=params)
    try:
        data = response.json()
        if len(data) <= 0:
            print("No result")
        else:
            print(f"[{data['id']}] {data['name']}")
    except ValueError:
        print("Not a valid JSON")


if __name__ == "__main__":
    import sys
    letter = sys.argv[1] if len(sys.argv) > 1 else ""
    search_user(letter)
