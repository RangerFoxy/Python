#!/usr/bin/env python3
import sys
import string

BETUK = string.ascii_lowercase


def main():
    if sys.argv[0].endswith("a-z.py"):
        print(BETUK)
    elif sys.argv[0].endswith("z-a.py"):
        print(BETUK[::-1])

##############################################################################


if __name__ == "__main__":
    main()