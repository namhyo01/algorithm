import sys
import heapq
input = sys.stdin.readline


n,m = map(int, input().split())
graph = [[] for _ in range(n+1)]
parent = [0 for _ in range(n+1)]

for _ in range(m):
    a,b,c, = map(int, input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

def dijkstra(s):
    global graph, parent
    distance = [sys.maxsize for _ in range(n+1)]
    q = []
    distance[s] = 0
    heapq.heappush(q,(0,s))
    while q:
        d,now = heapq.heappop(q)
        if distance[now] < d: continue
        for nn, nc in graph[now]:
            cost = d+nc
            if distance[nn] > cost: # 갱신해주자
                distance[nn] = cost
                heapq.heappush(q,(cost,nn))
                parent[nn] = now
dijkstra(1)
print(n-1)
for i in range(2,n+1):
    print(i, parent[i])