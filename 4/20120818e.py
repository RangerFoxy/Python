#!/usr/bin/env python3
# encoding: utf-8


def main():
    s = 0
    res = [i for i in range(1000) if i % 3 == 0 or i % 5 == 0]
    for i in res:
        s += i;
    print(s)

################################################################

if __name__ == '__main__':
    main()