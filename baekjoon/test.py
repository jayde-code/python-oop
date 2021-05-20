# a,b = map(int, input().split())
# print(a+b, a-b, sep='\n')
# a, b, c = map(int, input().split())
# print((a+b)%c, ((a%c)+(b%c))%c, (a*b)%c, ((a%c)*(b%c))%c, sep='\n')
# a, b, c = map(int, input().split())
# d, e, f = map(int, input().split())

# import random
#
# print(str(random.randint(0,999)).zfill(3))

# a = ['hong','gil','dong']
# b = list(enumerate(a))
# c = dict(enumerate(a))
# print(b)
# print(c)

letter = ['A', 'B', 'C']
for i in enumerate(letter, start=1):
    print(i)
print(letter)
