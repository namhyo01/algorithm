import sys
input = sys.stdin.readline
n,m = map(int,input().split())
data = [0 for _ in range(m)]
def dfs(now, cnt):
    if now == m:
        for i in range(m):
            print(data[i],end=' ')
        print()
        return
    for i in range(cnt,n):
        data[now] = i+1
        dfs(now+1,i+1)
dfs(0,0)
