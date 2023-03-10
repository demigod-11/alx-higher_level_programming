#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
argc = len(argv)
if argc < 2:
    print("{} arguments.".format(argc - 1))
else:
    x = 'argument' if argc == 2 else 'arguments'
    print("{} {}:".format(argc - 1, x))
    for i, j in enumerate(argv)
        print("{}: {}".format(i, j))
