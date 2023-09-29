#!/usr/bin/python3
"""sends a POST request to the passed URL
"""


if __name__ == "__main__":
    from urllib import request, parse
    import sys

    url = sys.argv[1]
    email = sys.argv[2]

    data = parse.urlencode({'email': email}).encode('utf-8')
    req = request.Request(url, data=data, method='POST')

    with request.urlopen(req) as response:
        body = response.read().decode('utf-8')
        print(body)
