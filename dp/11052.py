import sys, copy
input = sys.stdin.readline
N = int(input())
P = list(map(int,input().split()))
dp = copy.deepcopy(P)
for i in range(1, N):
    for j in range(i):
        dp[i] = max(dp[i], P[i-j-1]+dp[j])
print(dp[N-1])