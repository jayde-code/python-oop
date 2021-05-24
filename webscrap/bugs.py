class Bugs(object):
    def __init__(self, url):
        self.url = url

    def to_string(self):
        return f'URL : {self.url}'

    @staticmethod
    def main():
        while 1:
            menu = input('1 INPUT_URL\n2 OUTPUT_URL\n0 EXIT\n>> ')
            if menu == '1':
                bugs = Bugs(input('URL? '))
            elif menu == '2':
                print(bugs.to_string())
            elif menu == '0':
                break
            else:
                print('Wrong Number')
                continue


Bugs.main()
