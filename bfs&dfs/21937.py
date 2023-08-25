import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n,m = map(int, input().split())
graph = [[] for _ in range(n+1)]
check = [False for _ in range(n+1)]
for _ in range(m):
    a,b = map(int, input().split())
    graph[b].append(a)
X = int(input())
check[X] = True

cnt = -1

def dfs(X):
    global cnt
    cnt += 1
    for i in graph[X]:
        if not check[i]:
            check[i] = True
            dfs(i)
dfs(X)
print(cnt)


