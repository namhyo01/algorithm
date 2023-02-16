import sys
input = sys.stdin.readline
n,m = map(int,input().split())
check = [False for _ in range(9)]
num = [0 for _ in range(9)]

def dfs(cnt):
    if cnt == m:
        for i in range(m):
            print(num[i],end=' ')
        print()
        return
    for i in range(1,n+1):
        if not check[i]:
            check[i] = True
            num[cnt] = i
            dfs(cnt+1)
            check[i] = False
dfs(0)


