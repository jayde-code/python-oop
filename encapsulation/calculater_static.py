class CalculatorStatic(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def add(self):
        return self.first + self.second

    def sub(self):
        return self.first - self.second

    def mul(self):
        return self.first * self.second

    def div(self):
        return self.first / self.second


if __name__ == '__main__':
    cs = CalculatorStatic(5, 5)
    print(cs.add())
    print(cs.sub())
    print(cs.mul())
    print(cs.div())
