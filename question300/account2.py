import random


class Account(object):
    acc_count = 0

    def __init__(self, name, money):
        self.name = name
        self.money = money
        self.BANK_NAME = 'SC은행'
        self.acc_no = self.create_account_num()
        Account.acc_count += 1

    # 계좌번호는 3자리-2자리-6자리 형태로 랜덤하게 생성됩니다.
    @staticmethod
    def create_account_num():
        return str(random.randint(1, 999)).zfill(3) + '-' +\
               str(random.randint(1, 99)).zfill(2) + '-' + \
               str(random.randint(1, 999999)).rjust(6, "0")

    @staticmethod
    def create_account_num_2():
        # list comprehension
        ls = [str(random.randint(0, 9)) for i in range(3)]
        # for i in range(3):
        #     ls.append(str(random.randint(0, 9)))
        ls.append('-')
        for i in range(2):
            ls.append(str(random.randint(0, 9)))
        ls.append('-')
        for i in range(6):
            ls.append(str(random.randint(0, 9)))
        return ''.join(ls)  # '구분자'.join(리스트)

    @staticmethod
    def create_account_num_3():
        ls = []
        for i in range(13):
            if i == 3 or i == 6:
                ls.append('-')
            else:
                ls.append(str(random.randint(0, 9)))
        return ''.join(ls)

    def to_string(self):
        return f'{self.BANK_NAME}_{self.name}({self.acc_no}): {self.money}원'

    def deposit(self, dep):
        if dep > 1:
            self.money += dep
            print(f'{self.name}님의 입금액은 {dep}원이며, 잔고는 {self.money}원입니다.')
        else:
            print('입금은 1원 이상부터 가능합니다.')

    def withdraw(self, wit):
        if wit <= self.money:
            self.money -= wit
            print(f'{self.name}님의 출금액은 {wit}원이며, 잔고는 {self.money}원입니다.')
        else:
            print(f'현재 보유액({self.money}원) 이하만 가능합니다.')

    @classmethod
    def get_acc_count(cls):
        return cls.acc_count

    @staticmethod
    def main():
        ls = []
        while 1:
            print('\n' + '=' * 10 + ' SC BANK ATM MACHINE ' + '=' * 10)
            menu = input('1Create 2View 3Dep&With 4Drop 0EXIT >> ')
            if menu == '0':
                break
            elif menu == '1':
                ls.append(Account(input('name: '),
                                  int(input('money: '))))
            elif menu == '2':
                for i in ls:
                    print(i.to_string())
            elif menu == '3':
                for i, j in enumerate(ls):
                    print(f'|{i}| {j.to_string()}')
                who = int(input('Who are U? (input Number) >> '))
                dep_wit = input('Deposit or Withdraw? (+/-) : ')
                if dep_wit == '+':
                    for i, j in enumerate(ls):
                        if i == who:
                            j.deposit(int(input('money: ')))
                elif dep_wit == '-':
                    for i, j in enumerate(ls):
                        if i == who:
                            j.withdraw(int(input('money: ')))
            elif menu == '4':
                for i, j in enumerate(ls):
                    if j.acc_no == input('acc_no? '):
                        del ls[i]
            else:
                print('Wrong Num')


Account.main()
