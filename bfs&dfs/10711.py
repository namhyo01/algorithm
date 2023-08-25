import sys
input = sys.stdin.readline

dy = [-1,-1,-1,1,1,1,0,0]
dx = [0,1,-1,0,1,-1,1,-1]

h,w = map(int, input().split())
maps = [list(input().strip()) for _ in range(h)]
cq = []
cnt = 0
for i in range(h):
    for j in range(w):
        if '1' <= maps[i][j] <= '9':
            maps[i][j] = int(maps[i][j])
        else:
            maps[i][j] = False
            cq.append((i,j))


while True:
    nq = []
    cnt += 1
    change = False
    for y,x in cq:
        for i in range(8):
            ny = y+dy[i]
            nx = x+dx[i]
            if 0<=ny<h and 0<=nx<w and maps[ny][nx]:
                maps[ny][nx] -= 1
                if maps[ny][nx] == 0:
                    nq.append((ny,nx))
    if not nq: break
    cq = nq

print(cnt-1)


