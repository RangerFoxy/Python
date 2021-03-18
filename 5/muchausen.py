import datetime


def munchausen(hatvanyok,n):
    for szam in range(n):
        osszeg = 0
        for szamjegy in  str(szam):
            osszeg += hatvanyok[int(szamjegy)]
            if osszeg > szam:
                break
        if osszeg == szam:
            print(szam)


def main ():
    # hatvanyok = [0,1 ,4, 27, 256, 3125, 46656, 823543,16777216,387420489]
    hatvanyok = [0, 1 ** 1, 2 ** 2, 3 ** 3, 4 ** 4, 5 ** 5, 6 ** 6, 7 ** 7, 8 ** 8, 9 ** 9]
    t = datetime.datetime.now()
    munchausen(hatvanyok, 10000)
    print(datetime.datetime.now() - t)
    print()
    t = datetime.datetime.now()
    munchausen(hatvanyok,440000000)
    print(datetime.datetime.now()-t)


main()