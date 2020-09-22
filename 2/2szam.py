#!/usr/bin/env python3
# encoding: utf-8
'''
Olvassunk be két számot s írjuk ki a két szám összegét.

A) változat

A két számot parancssori argumentumként adjuk meg. Ha a felhasználó nem adja meg mindkét számot, akkor írjunk ki egy hibaüzenetet!

B) változat

A két számot interaktív módon kérjük be. (Tipp: használjuk az input() függvényt.)
'''


import sys

def commandLine(a, b):
    if len(sys.argv) < 2:
        print('Adj meg többet!')
    else:
        print(int(a) + int(b))

def fromInput():
    print('Add meg az első számot!')
    a = input()
    print('Add meg a második számot!')
    b = input()
    print(a + b)

def main():
    commandLine(sys.argv[1], sys.argv[2])
    fromInput()

################################################################

if __name__ == '__main__':
    main()