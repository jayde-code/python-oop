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

    @staticmethod   # static이 되며, self가 없다.
    def main():
        cs = CalculatorStatic(int(input('첫 번째 수 입력 : ')), int(input('두 번째 수 입력 : ')))
        print('[USE f string]')
        print(f'{cs.first} + {cs.second} = {cs.add()}')
        print(f'{cs.first} - {cs.second} = {cs.sub()}')
        print(f'{cs.first} * {cs.second} = {cs.mul()}')
        print(f'{cs.first} / {cs.second} = {cs.div()}')


CalculatorStatic.main()
