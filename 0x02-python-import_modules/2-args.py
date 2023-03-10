#!/usr/bin/python3
import sys

if len(sys.argv) > 1:
    print("{} argument".format(len(sys.argv) - 1))
    for i, j in enumerate(sys.argv):
        if i == 0:
            continue
        print("{}: {}".format(i, j))
else:
    print("0 arguments.")
