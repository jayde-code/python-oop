
print('[1부터 n까지의 합]', end='\n')
n = int(input('n? '))

sum = 0
for i in range(1, n + 1):
    sum += i

print(f'sum = {sum}')