#!/usr/bin/env python3


def main():
with open('/home/hallgato/Dani/string1.py', 'r') as f1, open('/home/hallgato/Dani/out.txt', 'w') as f2:
    for line in f1:
        if line.lstrip().startswith('#'):
            continue
        f2.write(line)
##############################################################################


if __name__ == "__main__":
    main()
