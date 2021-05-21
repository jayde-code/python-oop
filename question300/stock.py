class Stock(object):
    stock_list = []

    def __init__(self, code, name):
        self.code = code
        self.name = name
        # self.per = per
        # self.pbr = pbr
        # self.div_yield = div_yield

    def to_string(self):
        return f'종목코드: {self.code}, 종목명: {self.name}'

    @staticmethod
    def del_element(ls, input_code):
        for i, j in enumerate(ls):
            if j.code == input_code:
                del ls[i]

    @staticmethod
    def main():
        ls = []
        while 1:
            print('1 Create 2 Read 3 Update 4 Delete 0 EXIT')
            menu = input('INPUT>> ')
            if menu == '0':
                break
            elif menu == '1':
                ls.append(Stock(input('code? '), input('name? ')))
            elif menu == '2':
                for i in ls:
                    print(i.to_string())
            elif menu == '3':
                input_code = input('What code(Upt) : ')
                Stock.del_element(ls, input_code)
                ls.append(Stock(input_code, input('name? ')))
            elif menu == '4':
                input_code = input('What code(Del): ')
                Stock.del_element(ls, input_code)
            else:
                print('Wrong number')


Stock.main()
