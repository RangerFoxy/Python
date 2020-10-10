#!/usr/bin/env python3
# encoding: utf-8

def munchausen():
    print(0)
    for i in range(10000):
        if i == sum(int(x) ** int(x) for x in str(i)):
            print(i)

def main():
    munchausen()
    
################################################################

if __name__ == '__main__':
    main()