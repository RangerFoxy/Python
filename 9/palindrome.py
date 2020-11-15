#!/usr/bin/env python3

def palindrome(n):
    s = str(n).replace('0b', '')
    return s == s[::-1]

def main():
    counter = 0
    for i in range(1, 1000000):
        if palindrome(i) and palindrome(bin(i)):
            counter += i

    print(counter)
##############################################################################


if __name__ == "__main__":
    main()
