def add_func(f, s):
    return f + s


def sub_func(f, s):
    return f - s


def mul_func(f, s):
    return f * s


def div_func(f, s):
    return f / s


class Calculator:
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
    c = Calculator(4, 2)
    # c.setdata(2, 7)
    # print(c.add())
    # print(c.sub())
    # print(c.mul())
    # print(c.div())

    addVal = add_func(4, 4)
    subVal = sub_func(4, 4)
    mulVal = mul_func(4, 4)
    divVal = div_func(4, 4)
    print(addVal, subVal, mulVal, divVal)
