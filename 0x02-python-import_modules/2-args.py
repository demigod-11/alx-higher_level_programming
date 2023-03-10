#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
if len(argv) > 1:
    x = 'arguments' if len(argv) > 2 else 'argument'
    print("{:d} {}".format(len(argv) - 1, x))
    for i, j in enumerate(argv):
        if i == 0:
            continue
        print("{:d}: {}".format(i, j))
else:
    print("{} arguments.".format(len(argv) - 1))
