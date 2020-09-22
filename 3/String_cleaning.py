#!/usr/bin/env python3
# encoding: utf-8


def cleaner(s):
    return ' '.join(s.split())

def main():
    print(cleaner('      HELLO     NŐ   '))

################################################################

if __name__ == '__main__':
    main()