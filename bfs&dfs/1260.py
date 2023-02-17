import sys
from collections import deque
input = sys.stdin.readline
n, m, v  = map(int,input().split())
graph = [[False for _ in range(n+1)] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int, input().split())
    graph[a][b] = True
    graph[b][a] = True
checked = [False for _ in range(n+1)]
dfsList = []
bfsList = []
def prints(List):
    for i in List:
        print(i,end=' ')
def dfs(node):
    checked[node] = True
    dfsList.append(node)
    for i in range(1,n+1):
        if graph[node][i] and not checked[i]:
            dfs(i)
def bfs(node):
    checked = [False for _ in range(n+1)]
    queue=deque([node])
    checked[node] = True
    bfsList.append(node)
    while len(queue)>0:
        now = queue.popleft()
        for i in range(1,n+1):
            if graph[now][i] and not checked[i]:
                checked[i] = True
                bfsList.append(i)
                queue.append(i)

dfs(v)
prints(dfsList)
print()
bfs(v)
prints(bfsList)