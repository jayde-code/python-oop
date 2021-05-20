"""
이름, 전화번호, 이메일, 주소를 받아서
연락처 입력, 출력, 삭제하는 프로그램을 완성하시오.
"""


class Contacts(object):
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def get_contact(self):
        print(self.name, self.phone, self.email, self.address)

    @staticmethod
    def main():
        c = Contacts("Jay", "010-1234-5678", "Jay@gmail.com", "Seoul, Korea")
        c.get_contact()


Contacts.main()
