#!/usr/bin/env python3

def main():
    instructions = []
    with open('D:\Dokumentumok\input.txt') as f:
        for line in f:
            instructions.append([int(i) for i in line.split()])

    checksum = sum(max(line) - min(line) for line in instructions)

    print(checksum)

##############################################################################


if __name__ == "__main__":
    main()
