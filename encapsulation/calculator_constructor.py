class Calculator:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    # def setdata(self, first, second):
    #     self.first = first
    #     self.second = second

    def add(self):
        return self.first + self.second

    def sub(self):
        return self.first - self.second

    def mul(self):
        return self.first * self.second

    def div(self):
        if self.first >= self.second:
            return self.first / self.second
        else:
            return self.second / self.first


if __name__ == '__main__':
    c = Calculator(2, 7)
    # c.setdata(12, 7)
    # print(id(c))
    print(c.add())
    print(c.sub())
    print(c.mul())
    print(c.div())
