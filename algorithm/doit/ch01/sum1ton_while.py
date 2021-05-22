
print('[1부터 n까지의 합]', end='\n')
n = int(input('n? '))

sum = 0
i = 1
while i <= n:
    sum += i
    i += 1

print(f'sum = {sum}')