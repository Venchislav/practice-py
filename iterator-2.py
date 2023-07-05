# This...

# Custom Iterator

class CoupleElemListIterator:
    def __init__(self, lst):
        self.lst = lst
        self.i = 0

    def __next__(self):
        if self.i < len(self.lst) and len(self.lst) % 2 == 0:
            self.i += 2
            return self.lst[self.i - 2], self.lst[self.i - 1]
        else:
            raise StopIteration


class MyList(list):
    # Here we call our iterator
    def __iter__(self):
        return CoupleElemListIterator(self)


for i in MyList([1, 2, 3, 4, 5, 6]):
    print(i)

# =


def couple_generator(lst):
    i = 0
    for j in range(len(lst)):
        if i < len(lst) and len(lst) % 2 == 0:
            i += 2
            yield lst[i - 2], lst[i - 1]


cop_gen = couple_generator([1, 2, 3, 4, 5, 6])
for item in cop_gen:
    print(item)

# This
# 20 lines of code vs 10 lines :)
