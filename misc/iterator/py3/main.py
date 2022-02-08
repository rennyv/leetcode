# Write an iterator that generates x random numbers

import random


class XRandom:
    def __init__(self, length, limit) -> None:
        self.limit = limit
        self.length = length    
    
    def __iter__(self):
        self.count = 0
        return self
    
    def __next__(self):
        c = self.count + 1
        if c > self.limit:
            raise StopIteration

        self.count = c
        return [random.random() for _ in range(self.length)]



for i in XRandom(5, 4):
    print(i)