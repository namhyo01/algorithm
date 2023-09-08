import sys
input = sys.stdin.readline

n, m = map(int, input().split())
state = []
train = [[0 for _ in range(20)] for _ in range(n)]
for _ in range(m):
    t = list(map(int, input().split()))

    if t[0] == 1:
        train[t[1]-1][t[2]-1] = 1
        pass
    if t[0] == 2:
        train[t[1]-1][t[2]-1] = 0
        pass
    if t[0] == 3:
        for i in range(19,0,-1):
            train[t[1]-1][i] = train[t[1]-1][i-1]
        train[t[1]-1][0] = 0
        pass
    if t[0] == 4:
        for i in range(19):
            train[t[1]-1][i] = train[t[1] - 1][i+1]
        train[t[1]-1][19] = 0
        pass
cnt = 0
for i in range(n):
    if train[i] not in state:
        state.append(train[i])
        cnt += 1
print(cnt)