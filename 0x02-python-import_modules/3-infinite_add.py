#!/usr/bin/python3
import sys
summation = 0
for i, j in enumerate(sys.argv):
    if i == 0:
        continue
    summation += int(j)
print(summation)
