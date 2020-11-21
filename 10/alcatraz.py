#!/usr/bin/env python3

MAX = 600

def main():
    # Cellák kinyitása
    cells = [True for i in range(MAX + 1)]

    for i in range(2, MAX + 1):
        for j in range(i, MAX + 1, i):
            cells[j] = not cells[j]


    openedDoors = [str(index) for index, number in enumerate(cells[1:], start=1) if number]
    
    # Eredmény
    print("".join(openedDoors))

##############################################################################


if __name__ == "__main__":
    main()