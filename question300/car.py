class Car:
    def __init__(self, wheel, price):
        self.wheel = wheel
        self.price = price


if __name__ == '__main__':
    c = Car(2, 1000)
    print(c.wheel)
    print(c.price)
    