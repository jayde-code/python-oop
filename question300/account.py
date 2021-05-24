import random


class Account(object):
    # class variable
    account_count = 0

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.deposit_count = 0
        self.deposit_interest = 0
        self.deposit_log = []
        self.withdraw_log = []
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
            self.deposit_count += 1
            self.deposit_log.append(dep)
            print(f'{self.name} 님의 계좌에 {dep}원이 입금되어 잔액은 {self.balance}원 입니다.')
            if self.deposit_count % 5 == 0:
                self.deposit_interest = self.balance * 0.01
                self.balance += self.deposit_interest
                print(f'{self.deposit_interest}원의 이자가 발생했습니다.')
                print(f'현재 잔액 : {self.balance}')
        else:
            print('1원 이상부터 입금할 수 있습니다.')

    def withdraw(self, wit):
        if wit <= self.balance:
            self.balance -= wit
            self.withdraw_log.append(wit)
            print(f'{self.name} 님의 계좌에서 {wit}원이 출금되어 잔액은 {self.balance}원 입니다.')
        else:
            print('잔액이 부족합니다.')

    def display_info(self):
        print(f'은행명 : {self.bank}')
        print(f'고객명 : {self.name}')
        print(f'계좌번호 : {self.acc_no}')
        print(f'잔액 : {self.balance}')

    def deposit_history(self):
        for amount in self.deposit_log:
            print(f'{amount}원 입금')

    def withdraw_history(self):
        for amount in self.withdraw_log:
            print(f'{amount}원 출금')


    @staticmethod
    def main():
        a = Account("ㅅㅈ", 500000)
        b = Account("ㅂㅂ", 10000)
        c = Account("ㅎㅎ", 25000)
        acc_list = [a, b, c]
        # print(a.name, a.acc_no, a.balance)
        # print(b.name, b.acc_no, b.balance)
        # print(f'개설된 계좌수 : {a.get_account_num()}')
        # b.deposit(500)
        a.display_info()
        a.deposit(10000)
        a.deposit(20000)
        a.deposit(30000)
        a.deposit(50000)
        a.deposit(40000)

        a.withdraw(50000)
        a.withdraw(30000)
        a.withdraw(20000)
        a.withdraw(60000)
        # b.display_info()

        # for i in acc_list:
        #     if i.balance >= 20000:
        #         i.display_info()
        
        a.deposit_history()
        a.withdraw_history()


Account.main()
