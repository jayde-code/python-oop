def med3(a, b, c):
    if (a >= b >= c) or (c >= b >= a):
        return b
    elif (b >= a >= c) or (c >= a >= b):
        return a
    else:
        return c


print('세 정수의 중앙값?')
print(med3(int(input('a:')), int(input('b:')), int(input('c:'))))
