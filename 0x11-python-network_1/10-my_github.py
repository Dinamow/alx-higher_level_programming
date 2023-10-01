#!/usr/bin/python3
"""this is the api"""


if __name__ == "__main__":
    import sys
    import requests

    username = sys.argv[1]
    password = sys.argv[2]
    url = f"https://api.github.com/users/{username}"
    head = {'Accept': 'application/vnd.github+json',
            'X-GitHub-Api-Version': '2022-11-28',
            'Authorization': f"Bearer  {password}"}
    response = requests.get(url, headers=head)
    if response.status_code == 200:
        user_data = response.json()
        user_id = user_data["id"]
        if user_id:
            print(user_id)
    else:
        print("None")
