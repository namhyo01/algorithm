import sys
n = int(sys.stdin.readline())
dp = [[1]*10]*1001
for i in range(2,n+1):
    for j in range(10):
        if j == 0:
            dp[i][j] = 1
            continue
        dp[i][j] = (dp[i-1][j] + dp [i][j-1]) % 10007

ans = 0
for i in range(10):
    ans += dp[n][i]
print(ans%10007)
