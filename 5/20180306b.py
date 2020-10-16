#!/usr/bin/env python3
# encoding: utf-8

def aoc1(numbers):
    '''It returns the sum of the numbers which are equal to the next digit.'''
    res = 0
    nums = str(numbers)
    pre = int(nums[-1:])
    for c in [int(char) for char in nums]:
        if c == pre:
            res += c
        pre = c
    return res

def main():
    print(aoc1(122351))

################################################################

if __name__ == '__main__':
    main()