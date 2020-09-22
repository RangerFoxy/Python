#!/usr/bin/env python3
# encoding: utf-8
def intRev(s):
    #a = 0
    #while s > 0:
    #    a *= 10
    #    a += s % 10
    #   s //= 10
    #return a
    return int(str(s)[::-1])


def main():
    print(intRev(12568))
    

################################################################

if __name__ == '__main__':
    main()