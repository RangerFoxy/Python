#!/usr/bin/env python3
# encoding: utf-8

def valid(text, chars='ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'):
    li = [c for c in text]
    li2 = [c for c in chars]
    res = []
    for c in li:
        for ch in li2:
            if ch == c:
                res.append(c)
    str = ''
    return (str.join(res))

def main():
    print(valid('ASDk', '1234'))

################################################################

if __name__ == '__main__':
    main()