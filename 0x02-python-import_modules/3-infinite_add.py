#!/usr/bin/python3

if __name__ == "__main__":
    import sys

sum = 0

size = len(sys.argv) - 1

for i in range(1, size + 1):
    a = sys.argv[i]
    sum += int(a)
print("{}".format(sum))
