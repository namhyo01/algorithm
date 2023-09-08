import sys
input = sys.stdin.readline

dy = [1,-1,0,0]
dx = [0,0,1,-1]
r,c = map(int, input().split())

maps = [list(input().strip()) for _ in range(r)]
n = int(input())
h = list(map(int,(input().split())))

def bomb(height, dir):
    y, x = r - height, 0
    if dir == 1: # 왼쪽
        for k in range(c):
            if maps[y][k] == 'x': # 만약에 x라면 => 미네랄 파괴
                maps[y][k] = '.'
                x = k # x값 기록
                break
    else: # right 
        for k in range(c-1,-1,-1):  #거꾸로
            if maps[y][k] == 'x':
                maps[y][k] = '.'
                x = k
                break
    ret = []
    for k in range(4):
        ny = y + dy[k]
        nx = x + dx[k]
        if 0<= ny < r and 0<= nx < c and maps[ny][nx] == 'x': ret.append((ny,nx)) # 자기 클러스터 분리
    return ret

def fall(check, falling): # 떨어지는거 체크
    temp = 1
    flag = False
    while True:
        for y,x in falling:
            if y+temp == r-1: # 끝이라면
                flag = True
                break
            if maps[y+temp+1][x] == 'x' and not check[y+temp+1][x]: # 다른 미네랄을 떨어지다가 만날경우
                flag = True
                break
        if flag: break
        temp += 1 # 계속 떨구기
    for i in range(r-2,-1,-1):
        for j in range(c):
            if maps[i][j] == 'x' and check[i][j]:
                maps[i][j] = '.' # 역으로 가면서 떨어진거면 .으로 변경
                maps[i+temp][j] = 'x' # 떨어진 위치는 x라고 표시


def bfs(y,x): # 미네랄 떨어 트릴시 문제가 생기는지 탐색 
    ccq = [(y,x)]
    check = [[False for _ in range(c)] for _ in range(r) ]
    check[y][x] = True
    falling = []
    while True:
        nq = []
        for y,x in ccq:
            if y == r-1: return # 바닥이니 더 내려갈 곳이 없을테니?
            if maps[y+1][x] == '.': # 이거면 떨어져야지 계속
                falling.append((y,x))
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                if 0 <= ny < r and 0<=nx<c and maps[ny][nx] == 'x' and not check[ny][nx]: # 근처에 미네랄 하나 있다면 걔도 자기의 클러스터일테니
                    check[ny][nx] = True
                    nq.append((ny,nx))
        if not nq: break
        ccq = nq
    fall(check, falling)

dir = 1
while n:
    ret = bomb(h.pop, dir)
    print(ret)
    for y,x in ret:
        bfs(y,x)
    dir *= -1
    n -= 1

for i in maps:
    for j in i:
        print(j, end='')
    print()