class Contacts(object):
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email
        # self.address = address

    def to_string(self):
        return f'{self.name}, {self.phone}, {self.email}'

    @staticmethod
    def del_contact(name, ls):
        for i, j in enumerate(ls):
            if j.name == name:
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
                ls.append(Contacts(input('name: '),
                                   input('phone: '),
                                   input('email: ')))
            elif menu == '2':
                for i in ls:
                    print(i.to_string())
            elif menu == '3':
                if len(ls) > 0:
                    input_name = input('What name for UDT: ')
                    Contacts.del_contact(input_name, ls)
                    ls.append(Contacts(input_name,
                                       input('phone: '),
                                       input('email: ')))
                else:
                    print('[__Empty__]')
            elif menu == '4':
                if len(ls) > 0:
                    Contacts.del_contact(input('What name for DEL: '), ls)
                else:
                    print('[__EMPTY__]')
            else:
                print('[__WRONG NUMBER__]')
                continue


Contacts.main()
