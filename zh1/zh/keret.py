#!/usr/bin/env python3
import sys

INPUT = sys.argv[1]

def border(inp):
    line = inp.split('/n')
    width = max(len(s) for s in line)
    borders = ['+' + width * '-' + '+']
    for s in line:
        borders.append('|' + (s + ' ' * width)[:width] + '|')
    borders.append('+' + width * '-' + '+')
    print()
    print('/n'.join(borders))


def main():
    if sys.argv[1] == '':
        print('Add meg a fájlt!')
        sys.exit

    with open (INPUT, 'r'):
        border(INPUT)

    

##############################################################################


if __name__ == "__main__":
    main()
