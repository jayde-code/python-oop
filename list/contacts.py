"""
이름, 전화번호, 이메일, 주소를 받아서
연락처 입력, 출력, 삭제하는 프로그램을 완성하시오.
"""


class Contacts(object):
    # con_lists = []

    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def get_contact(self):
        return f'이름: {self.name}, 번호: {self.phone}, 이메일: {self.email}, 주소: {self.address}'

    @staticmethod
    def main():
        ls = []
        while 1:
            print('1. 주소록 추가\n2. 주소록 출력\n3. 주소록 삭제\n4. 주소록 수정\n0. 프로그램 종료')
            menu = input('입력 : ')
            if menu == '0':
                print('프로그램을 종료합니다.')
                break

            elif menu == '1':
                c = Contacts(input('이름? '), input('번호? '), input('이메일? '), input('주소? '))
                # Contacts.con_lists.append(c)
                ls.append(c)

            elif menu == '2':
                if len(ls) == 0:
                    print('입력된 연락처가 없습니다.')
                else:
                    # for contact in Contacts.con_lists:
                    #     print(contact.get_contact())
                    # ls = list(enumerate(ls))
                    for i, contact in enumerate(ls):
                        print(i, contact.get_contact())
                # if c is not None:
                #     print(c.get_contact())

            elif menu == '3':
                if len(ls) == 0:
                    print('입력된 연락처가 없습니다.')
                else:
                    for i, contact in enumerate(ls):
                        print(i, contact.get_contact())
                    del_index = int(input('삭제할 index_no: '))
                    for i, contact in enumerate(ls):
                        if i == del_index:
                            del ls[i]
                            print('정상적으로 삭제되었습니다.')

            elif menu == '4':
                if len(ls) == 0:
                    print('입력된 연락처가 없습니다.')
                else:
                    edit_name = input('수정할 이름: ')
                    edit_info = Contacts(edit_name, input('수정 전화번호: '), input('수정 이메일: '), input('수정 주소: '))
                    for i, j in enumerate(ls):
                        if j.name == edit_name:
                            del ls[i]
                            ls.append(edit_info)

            else:
                print('잘못 입력 하셨습니다.')
                continue

        # print(Contacts.con_lists)


Contacts.main()
