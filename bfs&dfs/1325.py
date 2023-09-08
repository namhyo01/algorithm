import sys
input = sys.stdin.readline

n,m = map(int, input().split())
maps = [[] for _ in range(n+1)]

for _ in range(m):
    a,b = map(int, input().split())
    maps[b].append(a)

max_cnt = 1
ans = []

def bfs(s):
    global n
    cnt = 1
    cq = [s]
    visited = [False for _ in range(n+1)]
    visited[s] = True

    while True: 
        nq = []
        for i in cq:
            for nn in maps[i]:
                if not visited[nn]:
                    visited[nn] = True
                    cnt += 1
                    nq.append(nn)
        if not nq: break
        cq = nq
    return cnt


for i in range(1,n+1):
    cnt = bfs(i)
    if cnt > max_cnt:
        max_cnt = cnt
        ans.clear()
        ans.append(i)
    elif cnt == max_cnt:
        ans.append(i)
print(*ans)

