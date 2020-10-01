#!/usr/bin/env python3
# encoding: utf-8


def main():
    a = 0
    for i in range(1, 101):
        a += i
    a *= a
    b = 0
    for i in range(1, 101):
        b += i*i
    print(a-b)

################################################################

if __name__ == '__main__':
    main()