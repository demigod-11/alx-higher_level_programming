#!/usr/bin/python3
for i in range(ord('z'), ord('a')-1, -1):
    letter = chr(i)
    if (i - ord('a')) % 2 == 0:
        letter = letter.upper()
    print("{:s}".format(letter), end="")
