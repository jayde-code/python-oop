class Stock(object):
    stock_list = []

    def __init__(self, name, code, per, pbr, div_yield):
        self.name = name
        self.code = code
        self.per = per
        self.pbr = pbr
        self.div_yield = div_yield

    def get_info(self):
        print(self.name, self.code, self.per, self.pbr, self.div_yield)

    @staticmethod
    def main():
        se = Stock("삼성전자", "005930", "15.79", "1.33", "2.83")
        hd = Stock("현대차", "005380", "8.70", "0.35", "4.27")
        lg = Stock("LG전자", "066570", "317.349", "0.69", "1.37")
        Stock.stock_list.append(se)
        Stock.stock_list.append(hd)
        Stock.stock_list.append(lg)
        # se.get_info()

        for stock in Stock.stock_list:
            print(f'종목코드: {stock.code} / PER: {stock.per}')


Stock.main()
