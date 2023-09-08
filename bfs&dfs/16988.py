import sys
from itertools import combinations
input = sys.stdin.readline
n,m = map(int, input().split())

maps = [list(map(int, input().split())) for _ in range(n)]
dy = [1,-1,0,0]
dx = [0,0,1,-1]
temp = []

for i in range(n):
    for j in range(m):
        if maps[i][j] == 0:
            temp.append((i,j)) # 0 위치 저장

def bfs(y,x):
    global maps, visited
    visited[y][x] = True
    cq = [(y,x)]
    ret = 1
    flag = True
    while True:
        nq = []
        for y,x in cq:
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                if 0<=ny<n and 0<=nx<m and not visited[ny][nx]:
                    if maps[ny][nx] == 0: flag = False
                    if maps[ny][nx] == 2:
                        visited[ny][nx] = True
                        ret += 1
                        nq.append((ny,nx))
        if not nq: break
        cq = nq
    return ret if flag else -1

def solve(p):
    global maps, visited
    ret = 0
    for y,x in p: maps[y][x] = 1

    for i in range(n):
        for j in range(m):
            if maps[i][j] == 2 and not visited[i][j]:
                cnt = bfs(i,j)
                if cnt != -1:
                    ret += cnt
    
    for y,x in p: maps[y][x] = 0 # 초기화
    return ret


ans = 0
for i in combinations(temp,2):
    visited = [[False] * m for _ in range(n)]
    ans = max(ans, solve(i))
print(ans)

