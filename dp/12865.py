import sys
input = sys.stdin.readline
n,k = map(int, input().split())
w = []
v = []
dp = [[0 for _ in range(k+1)] for _ in range(n+1)]

for _ in range(n):
    a, b = map(int, input().split())
    w.append(a)
    v.append(b)

for i in range(1, n+1):
    for j in range(1, k+1):
        if j >= w[i-1]:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w[i-1]]+v[i-1])
        else:
            dp[i][j] = dp[i-1][j]
print(dp[n][k])
