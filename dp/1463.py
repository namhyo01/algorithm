import sys
input = sys.stdin.readline
n = int(input())
dp = [999999999999999]*1000001
dp[0] = 0
dp[1] = 0
for i in range(2,n+1):
    if i%2==0:
        dp[i] = min(dp[i//2]+1,dp[i])
    if i%3==0:
        dp[i] = min(dp[i//3]+1,dp[i])
    dp[i] = min(dp[i],dp[i-1]+1)
print(dp[n])
