import sys
input = sys.stdin.readline


n = int(input())
front = []
back = []
dp = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(n):
        front.append(dp[i][0] + dp[j][1])
        back.append(dp[i][2] + dp[j][3])
front.sort()
back.sort()
res = 0

i,j = 0, len(back) - 1 
while i < len(front) and j >= 0:
    if front[i] + back[j] == 0:
        ni, nj = i+1, j-1

        while ni < len(front) and front[i] == front[ni]:
            ni += 1
        while nj >= 0 and back[j] == back[nj]:
            nj -= 1

        res += (ni-i) * (j-nj)
        i,j = ni,nj
    elif front[i] + back[j] > 0:
        j -= 1
    else:
        i += 1
print(res)