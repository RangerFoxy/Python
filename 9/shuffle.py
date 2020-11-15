#!/usr/bin/env python3
import random

def shuffled(l):
    return random.sample(l, len(l))

def main():
    l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print (shuffled(l)[-1])
    print(l)

##############################################################################


if __name__ == "__main__":
    main()
