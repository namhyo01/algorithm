import sys
import heapq
input = sys.stdin.readline
n = int(input())
q = []
for i in range(n):
    start, end = map(int, input().split())
    q.append([start,end])
q.sort()
hq = []
heapq.heappush(hq,q[0][1])
for i in range(1,n):
    if q[i][0] < hq[0]:
         heapq.heappush(hq,q[i][1])
    else:
        heapq.heappop(hq)
        heapq.heappush(hq,q[i][1])
    
print(len(hq))