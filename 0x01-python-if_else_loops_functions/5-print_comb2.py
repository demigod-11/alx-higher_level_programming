#!/usr/bin/python3
for i in range(0, 100):
    print(i if i > 10 else f"0{i:d}", end=', ' if i < 99 else '\n')
    
