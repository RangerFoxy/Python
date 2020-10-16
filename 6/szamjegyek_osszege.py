#!/usr/bin/env python3

def digits(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s

def main():
    print (digits(2**1000))

##############################################################################


if __name__ == "__main__":
    main()
