def bmi_function(h, w):
    return w / h ** 2 * 10000


class Bmi(object):
    def __init__(self, height, weight):
        self.h = height
        self.w = weight

    def get_bmi(self):
        return self.w / self.h ** 2 * 10000


if __name__ == '__main__':
    # b = Bmi(180, 80)
    # print(b.getBmi())
    # print('18.5 이하는 저체중, 18.5~25의 경우 정상, 25~30의 경우 과체중입니다.')
    print(bmi_function(180, 80))
