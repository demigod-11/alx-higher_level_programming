#!/usr/bin/python3
"""
    log parsing
"""


import sys


def print_info():
    print('File size: {:d}'.format(file_size))

    for scode, codetimes in sorted(status_codes.items()):
        if codetimes > 0:
            print('{}: {:d}'.format(scode, codetimes))


status_codes = {
    '200': 0,
    '301': 0,
    '400': 0,
    '401': 0,
    '403': 0,
    '404': 0,
    '405': 0,
    '500': 0
}

lc = 0
file_size = 0

try:
    for line in sys.stdin:
        if lc != 0 and lc % 10 == 0:
            print_info()

        pieces = line.split()

        try:
            status = int(pieces[-2])

            if str(status) in status_codes.keys():
                status_codes[str(status)] += 1
        except Exception as e:
            pass

        try:
            file_size += int(pieces[-1])
        except Exception as e:
            pass

        lc += 1

    print_info()
except KeyboardInterrupt:
    print_info()
    raise
