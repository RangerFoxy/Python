#!/usr/bin/env python3
# encoding: utf-8

def hangrend(word):
    mely = 'aáoóuú'
    magas = 'eéiíöőüű'
    me = 0
    ma = 0
    for c in word:
        if c in mely:
            me += 1
        if c in magas:
            ma += 1
    if ma != 0 and me != 0:
        return 'Vegyes hangrendű'
    if ma == 0:
        return 'Mély hangrendű'
    if me == 0:
        return 'magas hangrendű'

def main():
   word = input('Írj be egy szót: ')
   print(hangrend(word))
################################################################

if __name__ == '__main__':
    main()