#!/usr/bin/env python3
# encoding: utf-8

def triangle():
    counter = 0
    with open('haromszogek.txt', 'r') as f:
        lines = f.readlines()
        for s in lines:
            s.strip('\n')
            sor = s.split()
            a, b, c = sor
            if (int(a) + int(b) > int(c)) and (int(a) + int(c) > int(b)) and (int(b) + int(c) > int(a)):
                counter += 1

    return counter

            


def main():
    print('Szabályos háromszögek száma: ', triangle())

################################################################

if __name__ == '__main__':
    main()