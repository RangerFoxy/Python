#!/usr/bin/env python3
# encoding: utf-8
import json

def test(n):
    pass


def reader():
    with open('szamok.json', 'r') as f:
        numbers = json.load(f)
        for n in numbers:
            res = test(n)
            print(n, '->', res)



def main():
    reader()

################################################################

if __name__ == '__main__':
    main()