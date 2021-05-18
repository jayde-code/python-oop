class BodyMaxIndex:

    def __init__(self, weight, height):
        self.w = weight
        self.h = height

    # def setData(self, weight, height):
    #     self.weight = weight
    #     self.height = height

    def getBmi(self):
        return self.w / (self.h/100 * self.h/100)

if __name__ == '__main__':
    b = BodyMaxIndex(78, 179)
    # b.setData(80, 179)
    print('==============================================================')
    print(f'입력된 사용자의 BMI 지수는 {format(b.getBmi(), ".2f")} 입니다.')
    print('18.5 이하는 저체중, 18.5~25의 경우 정상, 25~30의 경우 과체중입니다.')
    print('==============================================================')