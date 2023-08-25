import sys
input = sys.stdin.readline

n = int(input())
h = list(map(int, input().split()))
h_sum = sum(h)

if h_sum % 3 != 0: print('NO') # 무조건 전체 개수는 3의 배수인 경우말고는 안나온다
else:
    check = 0 
    for i in h:
        check += i // 2 # 2의 개수를 체크
    if check >= h_sum // 3: print('YES')
    else: print('NO')

