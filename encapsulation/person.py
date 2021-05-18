"""
이름, 출생년도, 주소를 입력 받아서
회원가입한 사람의 이름, 만 나이, 주소를 출력하시오.
"""


class Person(object):
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def get_age(self):
        return 2021 - self.age

    @staticmethod
    def main():
        p = Person(input('이름 : '), int(input('출생년도(ex.1980) : ')), input('주소 : '))
        print(f'회원 가입한 분의 성함은 {p.name} 님 이며')
        print(f'나이는 만 {p.get_age()}세, 주소는 {p.address} 입니다.')


Person.main()
