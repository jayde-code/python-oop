a = int(input('a? '))
b = int(input('b? '))

if a > b:
    a, b = b, a # a와 b의 값을 교환(단일 대입문 사용)

sum = 0;
# for i in range(a, b+1):
#     sum += i
for i in range(a, b):
    print(f'{i} + ', end='')
    sum += i

print(f'{b} = ', end='')
sum += b

print(sum)