import random


class Account(object):
    acc_count = 0

    def __init__(self, name, money):
        self.name = name
        self.money = money
        self.BANK_NAME = 'SC은행'
        fst_no = str(random.randint(1, 999)).zfill(3)
        snd_no = str(random.randint(1, 99)).zfill(2)
        trd_no = str(random.randint(1, 999999)).zfill(6)
        self.acc_no = fst_no + '-' + snd_no + '-' + trd_no
        Account.acc_count += 1

    def deposit(self, dep):
        if dep > 1:
            self.money += dep
            print(f'입금액은 {dep}원이며, 잔고는 {self.money}원입니다.')
        else:
            print('입금은 최소 1원 이상만 가능합니다.')

    @classmethod
    def get_acc_count(cls):
        return cls.acc_count

    @staticmethod
    def main():
        a = Account("Jay", 60000)
        b = Account("Kay", 40000)
        print(a.BANK_NAME, a.name, a.acc_no, a.money)
        b.deposit(1)
        b.deposit(20)
        print(f'개설된 계좌수는 {Account.get_acc_count()} 개 입니다.')


Account.main()
