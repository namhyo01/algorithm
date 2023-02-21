import sys
input = sys.stdin.readline

n = int(input())
r = []
c = []
dp = [[0 for _ in range(n)] for _ in range(n)]
for _ in range(n):
    a ,b = map(int, input().split())
    r.append(a)
    c.append(b)
for cnt in range(n):
    for i in range(n-1-cnt):
        j = i + cnt + 1
        dp[i][j] = float('inf')
        for k in range(i, j):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j] + r[i]*c[k]*c[j])
print(dp[0][-1])