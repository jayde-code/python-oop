# a,b = map(int, input().split())
# print(a+b, a-b, sep='\n')
# a, b, c = map(int, input().split())
# print((a+b)%c, ((a%c)+(b%c))%c, (a*b)%c, ((a%c)*(b%c))%c, sep='\n')
# a, b, c = map(int, input().split())
# d, e, f = map(int, input().split())

# import random
#
#
# print(str(random.randint(0,999)).zfill(3))

# a = ['hong','gil','dong']
# b = list(enumerate(a))
# c = dict(enumerate(a))
# print(b)
# print(c)

# enumerate
# letter = ['A', 'B', 'C']
# for i in enumerate(letter, start=1):
#     print(i)
# print(letter)

# import random
# print(random.randint(1, 1000))

# from random import randint
# print(randint(1, 1000))

# from matplotlib import pyplot as plt
#
# print(plt.plot(x, y))

import matplotlib.pyplot

x = [1, 2, 3]
y = [3, 2, 1]

matplotlib.pyplot.plot(x, y)

# from matplotlib.pyplot import *
#
#
# print(plot(x, y))
