#!/usr/bin/python3
import sys
i = 1
if (len(sys.argv) == 1):
    print("0 arguments.")
else:
    print("{:d} argument:".format(len(sys.argv) - 1))
    while (i <= len(sys.argv) - 1):
        print("{:d}: {:s}".format(i, sys.argv[i]))
        i += 1
