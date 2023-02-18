import sys
input = sys.stdin.readline
n,k = map(int, input().split())
mod = 1000000000
dp = [[0 for _ in range(201)] for _ in range(201)]
for i in range(n+1):
    dp[i][1] = 1

for i in range(1,k+1):
    for j in range(0,n+1):
        for l in range(0,j+1):
            dp[j][i] += (dp[j-l][i-1])%mod

print(dp[n][k]%mod)