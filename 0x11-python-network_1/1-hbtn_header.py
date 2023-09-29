#!/usr/bin/python3
"""displays the value of the X-Request-Id
"""


if __name__ == "__main__":
    from urllib import request
    import sys

    if len(sys.argv) <= 1:
        exit()
    if not isinstance(sys.argv[1], str):
        exit()

    req = request.Request(sys.argv[1])

    with request.urlopen(req) as resp:
        print(resp.info()['X-Request-Id'])
