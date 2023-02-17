import sys
input = sys.stdin.readline
n,k = map(int, input().split())
coins = []
dp = [0 for _ in range(k+1)]
for _ in range(n):
    temp = int(input())
    coins.append(temp)
dp[0] = 1

for i in range(n):
    for j in range(coins[i],k+1):
        dp[j] += dp[j-coins[i]]
print(dp[k])