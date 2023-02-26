import sys
import heapq
input = sys.stdin.readline

def dijkstra(graph,n,d,c):
    queue = []
    dp = [10000000000 for _ in range(n+1)]
    heapq.heappush(queue,[0,c])
    dp[c] = 0
    while queue:
        distance, current = heapq.heappop(queue)
        if dp[current] < distance:
            continue
        for new_current,new_distance in graph[current]:
            new_distance += distance
            if dp[new_current] > new_distance:
                dp[new_current] = new_distance
                heapq.heappush(queue, [new_distance,new_current])
    cnt = ans = 0
    for i in range(1,n+1):
        if dp[i] != 10000000000:
            cnt+=1
            ans = max(ans,dp[i])
    print(cnt, ans)
t = int(input())
for _ in range(t):
    
    n,d,c = map(int, input().split())
    graph = [[] for i in range(n+1)]
    for _ in range(d):
        a,b,s = map(int, input().split())
        graph[b].append([a,s])
    dijkstra(graph,n,d,c)