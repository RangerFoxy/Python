#!/usr/bin/env python3
# encoding: utf-8
import csv
import operator


def volcano():
    with open('volcano.csv', 'r', encoding='iso-8859-1') as f:
        reader = csv.reader(f, delimiter=';')
        sortedReader = sorted(reader, key=operator.itemgetter(4))
        print('#NUMBER;RN;SN;VN;NAME;LOCATION;STATUS;LATX;NS;VF;LONGX;EW;ELEV;TYPE;TIMEFRAME')
        for s in sortedReader:
            line = ';'.join(s)
            if(line != '#NUMBER;RN;SN;VN;NAME;LOCATION;STATUS;LATX;NS;VF;LONGX;EW;ELEV;TYPE;TIMEFRAME'):
                print(line)

        


def main():
    volcano()

################################################################

if __name__ == '__main__':
    main()