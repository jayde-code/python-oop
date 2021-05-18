# def bmi_function(h, w):
#     return w / h ** 2 * 10000


class Bmi(object):
    def __init__(self, height, weight):
        self.h = height
        self.w = weight

    '''
    고도 비만 : 35 이상
    중(重)도 비만 (2단계 비만) : 30 - 34.9
    경도 비만 (1단계 비만) : 25 - 29.9
    과체중 : 23 - 24.9
    정상 : 18.5 - 22.9
    저체중 : 18.5 미만
    '''
    def get_bmi(self):
        return self.w / self.h ** 2 * 10000

    def get_status(self):
        bmi = self.get_bmi()

        if bmi < 18.4:
            status = '저체중'
        elif bmi < 23:
            status = '정상'
        elif bmi < 25:
            status = '과체중'
        elif bmi < 30:
            status = '경도 비만(1단계)'
        elif bmi < 35:
            status = '중도 비만(2단계)'
        else:
            status = '고도 비만'

        return status

    @staticmethod
    def main():
        b = Bmi(int(input('키 입력(cm)? ')), int(input('몸무게 입력(kg)? ')))
        print(f'입력하신 사용자의 BMI 지수는 {round(b.get_bmi(), 2)} 이며,')
        print(f'{b.get_status()} 입니다')


Bmi.main()
