#!/usr/bin/env python3
# encoding: utf-8
import time
start_time = time.time()


def main():
    #res = ''
    #for i in range(1, 16):
    #    res += str(i)
    #print(res)
    
    parts = []
    for i in range(1, 16):
        parts.append(str(i))
    res = ''.join(parts)
    print(res)
    print("--- %s seconds ---" % (time.time() - start_time))

################################################################

if __name__ == '__main__':
    main()