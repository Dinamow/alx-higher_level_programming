#!/usr/bin/python3
"""this is the api"""


if __name__ == "__main__":
    import sys
    import requests

    if len(sys.argv):
        print("None")
        exit()

    username = sys.argv[1]
    password = sys.argv[2]
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url, auth=(username, password))
    if response.status_code == 200:
        user_data = response.json()
        user_id = user_data["id"]
        print(user_id)
    else:
        print("None")
