class BugsMusic(object):
    # init이 제거된 것이 아니라 표기가 변경되었을 뿐이다.
    # def __init__(self, url):
    #     self.url = url

    url = ''

    def __str__(self):
        return self.url

    @staticmethod
    def main():
        bugs = BugsMusic()
        while 1:
            print('='*10 + ' MENU ' + '='*10)
            menu = input('1 INPUT_URL   2 OUTPUT_URL\n0 EXIT\n>> ')
            if menu == '1':
                # bugs = Bugs(input('URL? '))
                bugs.url = input('URL? ')
            elif menu == '2':
                print(f'Input URL is {bugs}')
            elif menu == '0':
                exit()
            else:
                print('Wrong Number')
                continue


BugsMusic.main()
