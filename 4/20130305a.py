#!/usr/bin/env python3
# encoding: utf-8


def xor(a, b):
    return bool(a) != bool(b)


def main():
    sztring1 = "python"
    sztring2 = None
    print(xor(sztring1, sztring2))

################################################################

if __name__ == '__main__':
    main()