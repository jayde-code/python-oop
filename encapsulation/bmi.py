class BodyMaxIndex:
    def setData(self, weight, height):
        self.weight = weight
        self.height = height
    def getBmi(self):
        return self.weight / (self.height/100 * self.height/100)

if __name__ == '__main__':
    b = BodyMaxIndex()
    b.setData(80, 179)
    print('==============================================================')
    print(f'입력된 사용자의 BMI 지수는 {format(b.getBmi(), ".2f")} 입니다.')
    print('18.5 이하는 저체중, 18.5~25의 경우 정상, 25~30의 경우 과체중입니다.')
    print('TEST')
    print('==============================================================')