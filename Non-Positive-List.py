class NonPositiveError(Exception):
    pass


class PositiveList(list):
    def append(self, elem):
        if elem > 0:
            super().append(elem)
        else:
            raise NonPositiveError()


p = PositiveList([1, 2, 3, 4, 5])
p.append(-5)
