import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

dx = [-2,-2,-1,-1,1,1,2,2]
dy = [-1,1,-2,2,-2,2,-1,1]

n,m = map(int, input().split())
x,y = map(int, input().split())
check = [[False for _ in range(n+1)] for _ in range(m+1)]
o = []
for _ in range(m):
    a,b = map(int, input().split())
    o.append((a,b))

cq = [(x,y)]
cnt = 0
check = [[-1 for _ in range(n+1)] for _ in range(n+1)]
ccheck = 0

check[x][y] = 0
while True:
    nq = []
    cnt += 1
    for nowx, nowy in cq:
        for i in range(8):
            newx = nowx + dx[i]
            newy = nowy + dy[i]
            if 1<=newx<=n and 1<=newy<=n and check[newx][newy] == -1:
                nq.append((newx,newy))
                check[newx][newy] = cnt
    if not nq: break
    cq = nq

for i, j in o:
    print(check[i][j], end = ' ')


            


