#!/usr/bin/python3
for i in range(0, 100):
    print(i if i > 10 else "0{}".format(i), end=', ' if i < 99 else '\n')
    
