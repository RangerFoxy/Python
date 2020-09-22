#!/usr/bin/env python3
# encoding: utf-8
import math

def digits(n):
    a = int(math.log10(n))+1
    return a

def main():
    print(digits(2**256))
    #print(len(str(2**256)))

################################################################

if __name__ == '__main__':
    main()