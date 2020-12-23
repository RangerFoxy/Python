#!/usr/bin/env python3
# encoding: utf-8

def border(lines):
        width = max(len(s) for s in lines)
        res = ['*' * (width + 4)]
        for s in lines:
            res.append('* ' + s + ' ' * (width -len(s)) + ' *')  
        res.append('*' * (width + 4))
        print('\n'.join(res))
            

def main():
    inp = 'hello world in a frame'
    lines = inp.split()
    border(lines)


################################################################

if __name__ == '__main__':
    main()