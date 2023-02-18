import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
T = int(input())
maps = [[False for _ in range(51)] for _ in range(51)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]
def dfs(x,y,M,N,checks):
    checks[y][x] = True
    for i in range(4):
        newx = x+dx[i]
        newy = y+dy[i]
        if newx >= 0 and newy >= 0 and newx < M and newy < N and not checks[newy][newx] and maps[newy][newx]:
            dfs(newx,newy,M,N,checks)

for _ in range(T):
    x, y, k = map(int, input().split())
    checks = [[False for _ in range(51)] for _ in range(51)]
    maps = [[False for _ in range(51)] for _ in range(51)]

    cnt = 0
    for _ in range(k):
        x1, y1 = map(int, input().split())
        maps[y1][x1] = True
    for i in range(x):
        for j in range(y):
            if not checks[j][i] and maps[j][i]:
                dfs(i,j,x,y,checks)
                cnt += 1
    print(cnt)
    

