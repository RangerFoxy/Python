#!/usr/bin/env python3
class Sor:
    def __init__(self):
        self.items = []

    def __str__(self):
        return str(self.items)

    def ures(self):
        return self.items == []

    def meret(self):
        return len(self.items)

    def hozzafuz(self, item):
        return self.items.insert(0, item)
    
    def torol(self):
        if self.ures():
            return 'None'
        return self.items.pop()


if __name__ == "__main__":
    s = Sor()
    print(s)
    print(s.ures())
    s.hozzafuz(1)
    s.hozzafuz(4)
    s.hozzafuz(5)
    print(s)
    print(s.meret())
    print(s.ures())
    x = s.torol()
    print(x)
    print(s)
    s.torol()
    s.torol()
    x = s.torol()
    print(x)
