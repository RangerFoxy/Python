#!/usr/bin/env python3


def main():
    with open('/home/hallgato/Dani/day4.txt', 'r') as f:
        db = 0
        for line in f:
            li = []
            parts = ["".join(sorted(list(s))) for s in line.split()]
            for s in parts:
                if s not in li:
                    li.append(s)
                else:
                    continue
            if li == parts:
                db += 1
        print(db)

##############################################################################


if __name__ == "__main__":
    main()
