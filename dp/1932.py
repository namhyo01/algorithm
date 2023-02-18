import sys
input = sys.stdin.readline
n = int(input())
triangle = []
for _ in range(n):
    triangle.append(list(map(int, input().split())))
dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
dp[0][0] = triangle[0][0]
for i in range(1,n):
    for j in range(i+1):
        if j==0:
            dp[i][j] += dp[i-1][j] + triangle[i][j]
            continue
        if j==i:
            dp[i][j] += dp[i-1][j-1] + triangle[i][j]

            continue
        dp[i][j] += max(dp[i-1][j-1],dp[i-1][j]) + triangle[i][j]
print(max(dp[n-1]))
