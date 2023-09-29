#!/usr/bin/python3
"""sends a POST request to the passed URL
"""


if __name__ == "__main__":
    from urllib import request, error
    import sys

    url = sys.argv[1]

    try:
        with request.urlopen(url) as response:
            body = response.read().decode('utf-8')
            print(body)
    except error.HTTPError as e:
        print(f"Error code: {e.code}")
