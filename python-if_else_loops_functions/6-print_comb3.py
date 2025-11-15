#!/usr/bin/python3
for i in range(0, 10):
    for j in range(i+1, 10):
        if i != 8:
            print("{:01d}{:01d}".format(i, j), end=", ")
        else:
            print("{:01d}{:01d}".format(i, j))
