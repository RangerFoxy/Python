#!/usr/bin/env python3


def zarojel(s):
    stack = []
    for c in s:
        if c == '(':
            stack.append(c)
        elif c == ')':
            if stack.pop() != '(':
                return False
        elif c == '{':
            stack.append(c)
        elif c == '}':
            if stack.pop() != '{':
                return False
        elif c == '[':
            stack.append(c)
        elif c == ']':
            if stack.pop() != '[':
                return False
        else:
            continue
    return stack == []


def main():
    print(zarojel('((5+3)*2+1)'))
    print(zarojel('{[(3+1)+2]+}'))
    print(zarojel('(3+{1-1)}'))
    print(zarojel('[1+1]+(2*2)-{3/3}'))
    print(zarojel('(({[(((1)-2)+3)-3]/3}-3)'))

##############################################################################


if __name__ == "__main__":
    main()
