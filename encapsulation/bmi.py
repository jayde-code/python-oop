# def bmi_function(h, w):
#     return w / h ** 2 * 10000


class Bmi(object):
    def __init__(self, height, weight):
        self.h = height
        self.w = weight

    def get_bmi(self):
        return self.w / self.h ** 2 * 10000

    @staticmethod
    def main():
        b = Bmi(int(input('키? ')), int(input('몸무게? ')))
        bmi = b.get_bmi()
        if bmi < 18.4:
            status = '저체중입니다.'
        elif bmi < 23:
            status = '정상입니다.'
        elif bmi < 25:
            status = '과체중입니다.'
        elif bmi < 30:
            status = '경도 비만(1단계)입니다.'
        elif bmi < 35:
            status = '중도 비만(2단계)입니다.'
        else:
            status = '고도 비만입니다.'
        print(f'BMI 지수 : {b.get_bmi()}')
        print(status)


Bmi.main()