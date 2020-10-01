#!/usr/bin/env python3
# encoding: utf-8
import sys
import random as r

UPTO = 100


def main():
    s = [r.randint(0, 9) for i in range(UPTO)]
    res = ''.join(map(str, s))
    chunks = [res[i:i+10] for i in range(0, len(res), 10)]
    for s in chunks:
        print(s)


################################################################

if __name__ == '__main__':
    main()