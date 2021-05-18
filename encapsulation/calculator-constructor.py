class Calculator:

    def __init__(self, first, second):
        self.first = first
        self.second = second

    def setdata(self, first, second):
        self.first = first
        self.second = second

    def add(self):
        return c.first + c.second

    def sub(self):
        return c.first - c.second

    def mul(self):
        return c.first * c.second

    def div(self):
        if c.first >= c.second:
            return c.first / c.second
        else:
            return c.second / c.first

if __name__ == '__main__':
    c = Calculator(2, 7)
    # c.setdata(12, 7)
    # print(id(c))
    print(c.add())
    print(c.sub())
    print(c.mul())
    print(c.div())
