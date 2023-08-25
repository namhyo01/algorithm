import sys
sys.setrecursionlimit(10**4)
input = sys.stdin.readline
INF = 100000
n,m = map(int, input().split())
s = list(map(int, input().split()))
dp = [sys.maxsize for _ in range(n+1)]

def solve(n):
    if n < 0: return INF
    if n == 0: return 0
    if dp[n] != sys.maxsize: return dp[n]
    for i in range(m):
        dp[n] = min(dp[n], solve(n-s[i]) + 1)
        for j in range(i+1,m): # 손은 두개다
            dp[n] = min(dp[n], solve(n- s[i] - s[j]) + 1)
    return dp[n]
ans = solve(n)
if ans >= INF: print(-1)
else: print(ans)


