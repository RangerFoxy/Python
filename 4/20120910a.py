#!/usr/bin/env python3
# encoding: utf-8


def main():
    mely = 'aáoóuú'
    magas = 'eéiíöőüű'
    word = input('Írj be egy szót: ')
    me = 0
    ma = 0
    for c in word:
        if c in mely:
            me += 1
        if c in magas:
            ma += 1
    if ma != 0 and me != 0:
        print('Vegyes hangrendű')
    if ma == 0:
        print('Mély hangrendű')
    if me == 0:
        print('magas hangrendű')

################################################################

if __name__ == '__main__':
    main()