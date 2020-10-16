#!/usr/bin/env python3
# encoding: utf-8


def szamjegyekOsszege():
    '''It returns the first 100 number's digits sum'''
    osszeg = 0
    for i in range(101):
        for c in str(i):
            osszeg += int(c)
    print(osszeg)

def main():
    szamjegyekOsszege()
################################################################

if __name__ == '__main__':
    main()