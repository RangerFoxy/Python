#!/usr/bin/env python3
# encoding: utf-8

def isPalindrome(s):
    return s == s[::-1]

def isPalindrome2(s):
    str = ''
    for i in s:
        str += i
    return s == str

def isPalindrome3(s):
    if len(s) < 2:
        return True
    if s[0] != s[-1]:
        return False
    return isPalindrome3(s[1:-1])

def main():
    print(isPalindrome('apa'))
    print(isPalindrome2('indul a görög aludni'))
    print(isPalindrome3('görög'))

################################################################

if __name__ == '__main__':
    main()