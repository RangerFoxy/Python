#!/usr/bin/env python3

TUNTETO = [0b01111001, 0b01101111,
           0b01110101, 0b01110100,
           0b01110101, 0b00101110,
           0b01100010, 0b01100101,
           0b00101111, 0b01100100,
           0b01010001, 0b01110111,
           0b00110100, 0b01110111,
           0b00111001, 0b01010111,
           0b01100111, 0b01011000,
           0b01100011, 0b01010001]

APPLE = [0b01010011, 0b01101111, 0b00100000, 0b01111001, 0b01101111, 0b01110101, 0b00100000, 0b01110100, 0b01101111, 0b01101111, 0b01101011,
         0b00100000, 0b01110100, 0b01101000, 0b01100101, 0b00100000, 0b01110100, 0b01101001, 0b01101101, 0b01100101, 0b00100000, 0b01110100,
         0b01101111, 0b00100000, 0b01110100, 0b01110010, 0b01100001, 0b01101110, 0b01110011, 0b01101100, 0b01100001, 0b01110100, 0b01100101,
         0b00100000, 0b01110100, 0b01101000, 0b01101001, 0b01110011, 0b00111111, 0b00100000,

         0b01010111, 0b01100101, 0b00100000, 0b01101100, 0b01101111, 0b01110110, 0b01100101, 0b00100000, 0b01111001, 0b01101111, 0b01110101,
         0b00101110]

def translate(s):
    for b in s:
        print(chr(b), end='')
    print()


def main():
    translate(TUNTETO)
    translate(APPLE)


##############################################################################


if __name__ == "__main__":
    main()
