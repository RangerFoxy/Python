#!/usr/bin/env python3
# encoding: utf-8


def main():
    res = sum([i for i in range(1000) if i % 3 == 0 or i % 5 == 0])
    print(res)

################################################################

if __name__ == '__main__':
    main()