class Contacts(object):
    # con_lists = []
    i = 1

    def __init__(self, name, phone, email, address):
        self.index = Contacts.i
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address
        Contacts.i += 1

    def get_cont(self):
        return f'{self.index}, {self.name}'

    @staticmethod
    def main():
        c = Contacts("j", 1, 2, 3)
        d = Contacts("k", 1, 2, 3)
        print(c.get_cont())
        print(d.get_cont())


Contacts.main()
