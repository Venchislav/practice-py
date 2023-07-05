from random import random


class RandomItem:
    def __init__(self, k):
        self.k = k
        self.i = 0

    # returns iter
    def __iter__(self):
        return self

    # iter must have __next__ method
    def __next__(self):
        if self.i < self.k:
            self.i += 1
            return random()
        else:
            raise StopIteration


for x in RandomItem(10):
    print(x)


# Code is well, but we can use generator func with yield

def random_generator(k):
    for i in range(k):
        yield random()


gen = random_generator(6)
print(type(gen))

for i in gen:
    print(i)
