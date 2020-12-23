#!/usr/bin/env python3
import string


def characters():
    txt = input('Adj meg egy stringet!')
    ch = [c for c in txt]
    ch.sort()
    res = ''
    alpha = string.ascii_lowercase
    for c in alpha:
        for character in ch:
            if character == c:
                res += c
        if res != '':
            print(res)
            res = ''


def main():
    characters()

##############################################################################


if __name__ == "__main__":
    main()
