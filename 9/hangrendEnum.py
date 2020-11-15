#!/usr/bin/env python3
from enum import Enum


class Hangrend(Enum):
    MELY = 'aáoóuú'
    MAGAS = 'eéiíöőüű'
    VEGYES = MELY + MAGAS
    HIBA = '1234567890'

def hangrend(word):
    me = False
    ma = False
    if word.strip() == '':
        return Hangrend.HIBA.name
    for c in word:
        if c in Hangrend.HIBA.value:
            return Hangrend.HIBA.name
        if not me:
            me = c in Hangrend.MELY.value
        if not ma:
            ma = c in Hangrend.MAGAS.value

    if me and ma:
        return Hangrend.VEGYES.name
    if me:
        return Hangrend.MELY.name
    if ma:
        return Hangrend.MAGAS.name 
    return Hangrend.HIBA.name 
      

        

def main():
#   word = input('Írj be egy szót: ')
#   print(hangrend(word))
   driver = ['ablak', 'erkély', 'kisvasút', 'magas', 'mély', 'Pfff']
   for s in driver:
        print(s + ': ' + hangrend(s))
   

##############################################################################


if __name__ == "__main__":
    main()
