from bs4 import BeautifulSoup
from urllib.request import urlopen


class BugsMusic(object):
    # __init__이 제거된 것이 아니라 표기가 변경되었을 뿐이다.
    # def __init__(self, url):
    #     self.url = url
    url = ''

    def __str__(self):
        return self.url

    def scrap(self):
        pass
        # https://music.bugs.co.kr/chart/track/realtime/total

    @staticmethod
    def main():
        bugs = BugsMusic()
        while 1:
            print('=' * 10 + ' MENU ' + '=' * 10)
            menu = input('1 INPUT_URL  2 RANK Top100 \n0 EXIT \n>> ')
            if menu == '1':
                # bugs = Bugs(input('URL? '))
                bugs.url = input('URL? ')
            elif menu == '2':
                print(f'Input URL is {bugs}')
                soup = BeautifulSoup(urlopen(bugs.url), 'lxml')
                n_artist = 0
                print('-' * 40 + ' RANK TOP 100 ' + '-' * 40)
                n_title = 0
                for li1, li2 in zip(soup.find_all(name='p', attrs=({"class": "title"})),
                                    soup.find_all(name='p', attrs=({"class": "artist"}))):
                    n_artist += 1
                    print(f'{str(n_artist).rjust(3, "0")}\' {li1.find("a").text} - {li2.find("a").text}')
                print('-' * 95)
            elif menu == '0':
                exit()
            else:
                print('Wrong Number')
                continue


BugsMusic.main()
