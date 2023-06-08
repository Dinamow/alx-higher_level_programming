#!/usr/bin/python3
if __name__ != "__main__":
    exit()
import sys
i = 0
for x in range(1, len(sys.argv)):
    i += int(sys.argv[x])
print("{:d}".format(i))
