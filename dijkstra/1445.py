import sys
from heapq import heappop, heappush
input = sys.stdin.readline

n,m = map(int, input().split())

dy = [0,0,1,-1]
dx = [1,-1,0,0]

l, g = [],[]
for i in range(n):
    l.append(list(input().rstrip()))
    for j in range(m):
        if l[i][j] == 'g':
            g.append((i,j))
        elif l[i][j] == 'S':
            sy, sx = i,j
        elif l[i][j] == 'F':
            fy, fx = i,j

for y,x in g:
    for i in range(4):
        ty = y+dy[i]
        tx = x+dx[i]
        if 0<=ty<n and 0<=tx<m and l[ty][tx] == '.':
            l[ty][tx] = '#'

q = []
heappush(q,(0,0,sy,sx))
v = [[0 for _ in range(m)] for _ in range(n)]
v[sy][sx] = 1


while q:
    a, b, y, x = heappop(q)
    for i in range(4):
        ty = y + dy[i]
        tx = x + dx[i]
        if 0<=ty<n and 0<=tx<m and not v[ty][tx]:
            v[ty][tx] = 1
            if l[ty][tx] == '.':
                heappush(q, (a,b,ty,tx))
            elif l[ty][tx] == '#':
                heappush(q, (a,b+1,ty,tx))
            elif l[ty][tx] == 'g':
                heappush(q, (a+1,b,ty,tx))
            else:
                print(a,b)
                break