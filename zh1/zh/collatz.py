#!/usr/bin/env python3


def collatz(number):
    if number % 2  == 0:
        return number //2
    else:
        result = 3 * number + 1
        return result


def main():
    n = 47
    li = []

    while n != 1:
        li.append(n)
        n = collatz(int(n))
    
    print('A sorozat hossza: ', len(li))
    for i in li:
        print(i, ' -> ', n, end='')    
    

##############################################################################


if __name__ == "__main__":
    main()
