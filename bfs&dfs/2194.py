import sys
input = sys.stdin.readline

dy = [0,0,1,-1]
dx = [1,-1,0,0]


n,m,a,b,k = map(int, input().split())
traps = []
for _ in range(k):
    traps.append(list(map(int, input().split())))
sty,stx = map(int, input().split())
rey,rex = map(int, input().split())
visited = [[False for _ in range(n)] for _ in range(m)]
