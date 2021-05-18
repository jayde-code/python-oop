class Human(object):
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def __del__(self):
        print('나의 죽음을 알리지 마라.')

    def setInfo(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def who(self):
        # print(self.name)
        # print(self.age)
        # print(self.gender)
        print("이름 : {} 나이 : {} 성별: {}".format(self.name, self.age, self.gender))

    @staticmethod
    def main():
        areum = Human("모름", 25, "모름")
        areum.setInfo("아름", 26, "여자")
        areum.who()
        del areum


Human.main()
