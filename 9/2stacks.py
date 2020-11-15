#!/usr/bin/env python3
class QueueWith2Stacks:
    def __init__(self):
        self.first = []
        self.second = []

    def __str__(self):
        return str(self.first + self.second)

    def is_empty(self):
        if self.size() == 0:
            return True
        return False

    def append(self, value):
        self.first.append(value)

    def popleft(self):
        if self.is_empty():
            return 'None'
        if not self.second:
            while self.first:
                self.second.append(self.first.pop())
        return self.second.pop()

    def size(self):
        return len(self.first) + len(self.second)

if __name__ == "__main__":
    s = QueueWith2Stacks()
    print(s)
    print(s.is_empty())
    s.append(1)
    s.append(4)
    s.append(5)
    print(s)
    print(s.size())
    print(s.is_empty())
    x = s.popleft()
    print(x)
    print(s)
    s.popleft()
    s.popleft()
    x = s.popleft()
    print(x)
