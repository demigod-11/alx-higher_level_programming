#!/usr/bin/python3
import sys

if __name == "__main__":
    if len(sys.argv) > 1:
        print("{:d} argument".format(len(sys.argv) - 1))
        for i, j in enumerate(sys.argv):
            if i == 0:
                continue
            print("{:d}: {}".format(i, j))
    else:
        print("0 arguments.")
