#!/usr/bin/python3
i = chr

for i in range(ord('a'), ord('z') + 1):
    if i != ord('q') and i != ord('e'):
        print("{}".format(chr(i)), end='')
