class ExtendedStack(list):
    def __init__(self):
        self.x = list.pop()
        self.x2 = list.pop()

    def sum(self):
        list.append(self.x + self.x2)

    def sub(self):
        list.append(self.x - self.x2)

    def mul(self):
        list.append(self.x * self.x2)

    def div(self):
        list.append(self.x // self.x2)



