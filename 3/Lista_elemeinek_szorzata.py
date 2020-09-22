#!/usr/bin/env python3
# encoding: utf-8


def multiplication(l):
    a = 1
    for i in l:
        a *= i
    return a

def main():
    li = [1, 2, 4, 5]
    print(multiplication(li))

################################################################

if __name__ == '__main__':
    main()