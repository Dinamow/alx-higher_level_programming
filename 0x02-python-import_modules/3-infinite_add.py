#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    lenth = len(sys.argv)
    i, loop = 0, 0

    if lenth == 1:
        print("{:d}".format(0))
    else:
        while (loop < lenth - 1):
            loop += 1
            i += int(sys.argv[loop])
        print("{:d}".format(i))
