#!/usr/bin/env python3
import statistics

def median(l):
    return statistics.median(l);

def main():
    print (median([1, 2, 3, 4, 5]))
    print (median([3, 1, 2, 5, 3]))
    print (median([1, 300, 2, 200, 1]))
    print (median([3, 6, 20, 99, 10, 15]))


##############################################################################


if __name__ == "__main__":
    main()
