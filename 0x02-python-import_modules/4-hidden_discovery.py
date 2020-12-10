#!/usr/bin/python3

if __name__ == "__main__":
    import hidden_4
    import dis

a = dir(hidden_4)
size = len(a)

for i in range(0, size):
    if (a[i][0] != '_'):
        print("{}".format(a[i]))
