#!/usr/bin/env python3
# encoding: utf-8

def shellProgramHelyett():
    s = 0
    for i in range(101):
        s += i
    print(s)

def szamjegyekOsszege():
    osszeg = 0
    for i in range(101):
        for c in str(i):
            osszeg += int(c)
    print(osszeg)

def main():
    shellProgramHelyett()
    szamjegyekOsszege()
################################################################

if __name__ == '__main__':
    main()