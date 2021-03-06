#!/usr/bin/env python3
# encoding: utf-8

def munchausen():
    '''It returns the Munchausen numbers below 10000'''
    print(0)
    for i in range(10000):
        if i == 0:
            continue
        if i == sum(int(x) ** int(x) for x in str(i)):
            print(i)

def main():
    munchausen()
    
################################################################

if __name__ == '__main__':
    main()