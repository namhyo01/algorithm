import sys
input = sys.stdin.readline

n = int(input())
cost = [list(map(int, input().split())) for _ in range(n)]
ans = sys.maxsize
for i in range(3):
    dp = [[sys.maxsize for _ in range(3)] for _ in range(n)]
    dp[0][i] = cost[0][i] # 시작값 고정
    for j in range(1,n):
        dp[j][0] = cost[j][0] + min(dp[j-1][1], dp[j-1][2])
        dp[j][1] = cost[j][1] + min(dp[j-1][0], dp[j-1][2])
        dp[j][2] = cost[j][2] + min(dp[j-1][0], dp[j-1][1])
    for k in range(3):
        if i != k: # 마지막 방이 처음이랑 다르면
            ans = min(ans, dp[n-1][k])
print(ans)