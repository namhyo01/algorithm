import sys
input = sys.stdin.readline
n = int(input())
mod = 9901
dp = [[0 for _ in range(3)] for _ in range(n+1)]
dp[1][0] = 1
dp[1][1] = 1
dp[1][2] = 1
for i in range(2,n+1):
    dp[i][0] = (dp[i-1][1] + dp[i-1][2] + dp[i-1][0])%mod
    dp[i][1] = (dp[i-1][0] + dp[i-1][2])%mod
    dp[i][2] = (dp[i-1][0] + dp[i-1][1])%mod
print(sum(dp[n])%mod)
