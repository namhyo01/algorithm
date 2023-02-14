import sys
input = sys.stdin.readline

n = int(input())
dx = [0,0,1,-1]
dy = [1,-1,0,0]
all = 0
cnt = 0
maps = [[0 for _ in range(n)]for _ in range(n)]
visited = [[False for _ in range(n)] for _ in range(n)]

for i in range(n):
    x = input()
    for j in range(n):
        maps[i][j] = int(x[j])

def dfs(x,y):
    global cnt
    global visited
    global maps
    cnt+=1
    visited[x][y] = True
    for i in range(4):
        newx = x+dx[i]
        newy = y+dy[i]
        if newx>=0 and newy>=0 and newx<n and newy<n and maps[newx][newy]==1 and not visited[newx][newy]:
            dfs(newx, newy)
ans = []
for i in range(n):
    for j in range(n):
        if not visited[i][j] and maps[i][j] == 1:
            cnt = 0
            all+=1
            dfs(i,j)
            ans.append(cnt)
ans.sort()
print(all)
for i in range(all):
    print(ans[i])
