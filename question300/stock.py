class Stock(object):
    def __init__(self, name, code, per, pbr, dividend):
        self.name = name
        self.code = code
        self.per = per
        self.pbr = pbr
        self.dividend = dividend

    def set_name(self, name):
        self.name = name

    def set_code(self, code):
        self.code = code

    def get_name(self):
        return self.name

    def get_code(self):
        return self.code

    def set_per(self, per):
        self.per = per

    def set_pbr(self, pbr):
        self.pbr = pbr

    def set_dividend(self, dividend):
        self.dividend = dividend

    @staticmethod
    def main():
        ss = Stock("삼성전자", "005930", 15.79, 1.33, 2.83)
        hd = Stock("현대차", "005380", 8.70, 0.35, 4.27)
        lg = Stock("LG전자", "066570", 317.34, 0.69, 1.37)
        item = [ss, hd, lg]

        for i in item:
            print(i.code, i.per)


Stock.main()
