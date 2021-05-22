print('+와 -를 번갈아 출력합니다.')
n = int(input('n? '))

for _ in range(n // 2):
    print('+-', end='') # +-를 n//2개 출력

if n % 2:
    print('+', end='') # 홀수인 경우 +를 출력
