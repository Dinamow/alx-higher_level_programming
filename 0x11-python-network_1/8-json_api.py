#!/usr/bin/python3
"""
post req to the API 'http://0.0.0.0:5000/search_user'
"""

if __name__ == "__main__":
    import requests
    import sys
    url = "http://0.0.0.0:5000/search_user"
    try:
        params = {'q': sys.argv[1]}
    except IndexError:
        print("No result")
        exit()
    response = requests.post(url, data=params)
    try:
        data = response.json()
        if len(data) <= 0:
            print("No result")
        else:
            print(f"[{data['id']}] {data['name']}")
    except ValueError:
        print("Not a valid JSON")
