#!/usr/bin/env python3
# encoding: utf-8
import sys

def main():
    h = eval(input("Add meg a gyémánt magasságát: "))
    if h % 2 == 0:
        print('Páratlan számot kell megadni!')
        sys.exit()

    for i in range(1, h, 2):
        print(' '*(h//2 - i//2), '*'*i)
    for i in range(h, 0, -2):
        print(' '*(h//2 - i//2), '*'*i)

################################################################

if __name__ == '__main__':
    main()