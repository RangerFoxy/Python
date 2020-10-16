#!/usr/bin/env python3

def anagrams(s1, s2):
    if sorted(s1) == sorted(s2):
        print ('Anagrammák')
    else:
        print ('Nem anagrammák')

def dic(s):
    d = {}
    for c in s:
        if c in d:
            d[c] += 1
        else:
            d[c] = 1
    return d

def anagrams2(s1, s2):
    if len (s1) != len(s2):
        print ('Nem anagrammák')
    else:
        if dic(s1) == dic(s2):
            print ('Anagrammák')
        else:
            print ('nem anagrammák')

def normalize(s):
    sr = s.replace(' ', '')
    return sr.lower()

def main():
    anagrams('listen','silent')
    print (normalize('Clint Eastwood'))
    anagrams2('listen', 'silent')

##############################################################################


if __name__ == "__main__":
    main()
