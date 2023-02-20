import sys
input = sys.stdin.readline

n = int(input())
chus = list(map(int, input().split()))
m = int(input())
balls = list(map(int, input().split()))
dp = [[False for _ in range((i+1)*500+1)] for i in range(n+1)]

def dfs(cnt, weight):
    if cnt > n:
        return
    if dp[cnt][weight]:
        # 굳이 더 셀 필요가 없으니
        return 
    dp[cnt][weight] = True
    dfs(cnt+1, weight)
    dfs(cnt+1, abs(weight - chus[cnt-1]))
    dfs(cnt+1, weight + chus[cnt-1])

dfs(0,0)
for ball in balls:
    if ball > 30 * 500:
        print('N', end = ' ')
        continue
    if dp[n][ball]:
        print('Y',end = ' ')
    else:
        print('N',end=' ')

