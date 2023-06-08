#!/usr/bin/python3
import sys
i = 1
if (len(sys.argv) == 1):
    print("0 arguments.")
elif (len(sys.argv) == 2):
    print("1 argument:\n1: {:s}".format(sys.argv[1]))
else:
    print("{:d} arguments:".format(len(sys.argv) - 1))
    while (i <= len(sys.argv) - 1):
        print("{:d}: {:s}".format(i, sys.argv[i]))
        i += 1
