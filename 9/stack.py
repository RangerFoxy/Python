#!/usr/bin/env python3
class Verem:
    def __init__(self):
        self.items = []

    def __str__(self):
        return str(self.items)

    def ures(self):
        return self.items == []

    def betesz(self, item):
        self.items.append(item)

    def kivesz(self):
        if self.ures():
            return 'None'
        return self.items.pop()

    def meret(self):
        return len(self.items)


if __name__ == "__main__":
    v = Verem()
    print(v)
    print(v.ures())
    v.betesz(1)
    v.betesz(4)
    v.betesz(5)
    print(v)
    print(v.meret())
    print(v.ures())
    x = v.kivesz()
    print(x)
    print(v)
    v.kivesz()
    v.kivesz()
    x = v.kivesz()
    print(x)
    