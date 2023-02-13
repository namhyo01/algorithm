import sys
from collections import deque
input = sys.stdin.readline
n,k = map(int, input().split())
queue = deque([(n,0)])
visited = [False]*100001
while True:
    now, cnt = queue.popleft()
    visited[now] = True
    if now == k:
        print(cnt)
        break
    if now+1<=100000 and not visited[now+1]:
        queue.append((now+1,cnt+1))
    if now != 0:
        if now*2<=100000 and not visited[now*2]:
            queue.append((now*2,cnt+1))
        if not visited[now-1]:
            queue.append((now-1,cnt+1))

