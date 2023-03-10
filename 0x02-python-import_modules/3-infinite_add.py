#!/usr/bin/python3
import sys
if __name__ == "__main__":
    summation = 0
    for i, j in enumerate(sys.argv):
        if i == 0:
            continue
        summation += int(j)
    print(summation)
