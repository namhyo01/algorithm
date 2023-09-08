import sys
from itertools import combinations
input = sys.stdin.readline

'''
    구역을 두개의 선거구로 나누자
    일단 모두 인접해야한다 같은 선거구면
    공평하게 나누기 위해 최소한의 인구차를 나게 하자
    
'''

n = int(input())
pop = [0]+list(map(int, input().split()))
graph = {}
for i in range(1,n+1):
    a = list(map(int, input().split()))
    graph[i] = a[1:]

V = [i for i in range(1,n+1)]
ans = sys.maxsize

def isConnected(section):
    global graph
    cq = [section[0]]
    visited = [False for _ in range(n+1)]
    visited[section[0]] = True
    while True:
        nq = []
        for s in cq:
            for v in graph[s]:
                if v in section and not visited[v]:
                    nq.append(v)
                    visited[v] = True
        if not nq: break
        cq = nq
    for s in section:
        if not visited[s]: return False # 같은 섹션 안이라면 무조건 방문해야한다 모두
    return True

for i in range(1,n):
    for s1 in combinations(V,i):
        s2 = [j for j in V if j not in s1]
        # 연결되는지를 체크
        if isConnected(s1) and isConnected(s2):
            ans = min(ans, abs(sum(pop[s] for s in s1) - sum(pop[s] for s in s2)))
if ans == sys.maxsize: print(-1)
else: print(ans)





