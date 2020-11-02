#!/usr/bin/env python3

INPUT = '/home/dani/Letöltések/vmi.txt'

def main():
    with open(INPUT, 'r') as f:
        a = f.readlines()
        db = 0
        for line in a:
            b = line.split()
            c = set(b)
            if len(b) == len(c):
                db += 1

    print(db)

##############################################################################


if __name__ == "__main__":
    main()