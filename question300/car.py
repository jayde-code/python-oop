class Car:
    def __init__(self, wheel, price):
        self.wheel = wheel
        self.price = price


class Bicycle(Car):
    def __init__(self, wheel, price, engine):
        super().__init__(wheel, price)
        self.engine = engine

    def get_info(self):
        print("바퀴수:", self.wheel)
        print("가격:", self.price)


class AutoVehicle(Car):
    def __init__(self, wheel, price):
        super().__init__(wheel, price)

    def get_info(self):
        print("바퀴수:", self.wheel)
        print("가격:", self.price)


if __name__ == '__main__':
    # car = AutoVehicle(4, 1000)
    # car.get_info()
    bicycle = Bicycle(2, 100, "시마노")
    bicycle.get_info()
