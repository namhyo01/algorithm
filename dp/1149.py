import sys
input = sys.stdin.readline
n = int(input())
house = []
dp = [[0 for _ in range(3)] for _ in range(n+1)]
for _ in range(n):
    house.append(list(map(int, input().split())))
for i in range(len(house)):
    dp[i+1][0] = house[i][0] + min(dp[i][1], dp[i][2])
    dp[i+1][1] = house[i][1] + min(dp[i][0], dp[i][2])
    dp[i+1][2] = house[i][2] + min(dp[i][0], dp[i][1])
print(min(dp[n]))