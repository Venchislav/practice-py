class MoneyBox:
    curent_cap = 0

    def __init__(self, capacity):
        self.capacity = capacity

    def can_add(self, v):
        if v + self.curent_cap <= self.capacity:
            return True
        return False

    def add(self, v):
        if self.can_add(v):
            self.curent_cap += v


Cap = MoneyBox(10)
print(Cap.capacity)
print(Cap.can_add(8))
print(Cap.curent_cap)
print(Cap.add(8))
print(Cap.curent_cap)
print(Cap.can_add(3))
print(Cap.curent_cap)
print(Cap.can_add(2))
print(Cap.curent_cap)
print(Cap.capacity)
