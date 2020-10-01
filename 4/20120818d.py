#!/usr/bin/env python3
# encoding: utf-8
import string

def main():
    #1. feladat
    li = ['auto', 'villamos', 'metro']
    res = [s.upper() + '!' for s in li]
    print(res)
    #2. feladat
    li = ['aladar', 'bela', 'cecil']
    res = [s. capitalize() for s in li]
    print(res)
    #3. feladat
    res = [0 for i in range(10)]
    print(res)
    #4. feladat
    li = [i for i in range(1, 11)] 
    res = [i+i for i in li]
    print(res)
    #5. feladat
    li = [str(c) for c in range(1, 11)]
    res = [int(c) for c in li]
    print(res)
    #6. feladat
    li = '1234567'
    res = [int(c) for c in li]
    print(res)
    #7. feladat
    li = 'The quick brown fox jumps over the lazy dog'
    res = [len(s) for s in li.split()]
    print(res)
    #8. feladat
    li = 'python is an awesome language'
    res = [s[0]  for s in li.split()]
    print(res)
    #9. feladat
    li = 'The quick brown fox jumps over the lazy dog'
    res = [(s, len(s)) for s in li.split()]
    print(res)
    #10. feladat
    res = [i for i in range(10) if i % 2 == 0]
    print(res)
    #11. feladat
    res = [i*i for i in range(20) if i*i % 2 == 0]
    print(res)
    #12. feladat
    res = [i*i for i in range(20) if str(i*i)[-1] == '4']
    print(res)
    #13. feladat
    li = string.ascii_uppercase
    res = [''.join(li)]
    print(res)
    #14. feladat
    li = [' apple ', ' banana ', ' kiwi']
    res = [s.strip() for s in li]
    print(res)
    #15. feladat
    li = [1, 0, 1, 1, 0, 1, 0, 0]
    res = ''.join(map(str, li))
    print(res)


################################################################

if __name__ == '__main__':
    main()