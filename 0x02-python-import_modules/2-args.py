#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    if len(argv) > 1:
        print("{:d} argument".format(len(argv) - 1))
        for i, j in enumerate(argv):
            if i == 0:
                continue
            print("{:d}: {}".format(i, j))
    else:
        print("0 arguments.")
