import sys
input = sys.stdin.readline
n = int(input())
A = list(map(int, input().split()))
dp = [0 for _ in range(n+1)]
for i in range(n):
    dp[i] = A[i]
    for j in range(i):
        if A[i] > A[j]:
            dp[i] = max(dp[j]+A[i],dp[i])
print(max(dp))