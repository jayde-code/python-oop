import random


class Account(object):
    # class variable
    account_count = 0

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.bank = "SC은행"
        n1 = str(random.randint(0, 999)).zfill(3)
        n2 = str(random.randint(0, 99)).zfill(2)
        n3 = str(random.randint(0, 999999)).zfill(6)
        self.acc_no = n1 + '-' + n2 + '-' + n3

        Account.account_count += 1

    @classmethod
    def get_account_num(cls):
        return cls.account_count

    def deposit(self, dep):
        if dep >= 1:
            self.balance += dep
            print(f'{self.name} 님의 계좌에 {dep}원이 입금되어 잔액은 {self.balance}원 입니다.')
        else:
            print('1원 이상부터 입금할 수 있습니다.')

    def withdraw(self, wit):
        if wit <= self.balance:
            self.balance -= wit
            print(f'{self.name} 님의 계좌에서 {wit}원이 출금되어 잔액은 {self.balance}원 입니다.')
        else:
            print('잔액이 부족합니다.')

    def display_info(self):
        print(f'은행명 : {self.bank}')
        print(f'고객명 : {self.name}')
        print(f'계좌번호 : {self.acc_no}')
        print(f'잔액 : {self.balance}')

    @staticmethod
    def main():
        a = Account("ㅅㅈ", 50000)
        b = Account("ㅂㅂ", 10000)
        print(a.name, a.acc_no, a.balance)
        print(b.name, b.acc_no, b.balance)
        print(f'개설된 계좌수 : {a.get_account_num()}')
        b.deposit(500)
        a.withdraw(10000)
        b.withdraw(20000)
        a.display_info()
        b.display_info()


Account.main()
