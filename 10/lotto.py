#!/usr/bin/env python3

LOTTO = 45

def lotto(numSum, product):
    for i in range(1, LOTTO + 1):
        for j in range(i + 1, LOTTO + 1):
            for k in range(j + 1, LOTTO + 1):
                for l in range(k + 1, LOTTO + 1):
                    for m in range(l + 1, LOTTO + 1):
                        for n in range(m + 1, LOTTO + 1):
                            if ((i + j + k + l + m + n) == numSum and (i * j * k * l * m * n) == product):
                                return (i, j, k, l, m, n)

def main():
    winningNums = lotto(90, 996300)
    print(winningNums)

##############################################################################


if __name__ == "__main__":
    main()