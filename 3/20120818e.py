#!/usr/bin/env python3
# encoding: utf-8
#Állapítsuk meg azon 1000-nél kisebb számok összegét, melyek 3-nak vagy 5-nek a többszörösei.


def main():
    s = 0
    for i in range(1, 1000):
        if i % 3 == 0 or i % 5 == 0:
            s += i
    print(s)

################################################################

if __name__ == '__main__':
    main()