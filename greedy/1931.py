import sys
input = sys.stdin.readline
n = int(input())
rooms = []
for i in range(n):
    rooms.append(list(map(int, input().split())))
rooms.sort(key=lambda x: (x[1],x[0]))
cnt = 1
start,end = rooms[0][0], rooms[0][1]
for i in range(1,n):
    if rooms[i][0] >= end:
        end = rooms[i][1]
        cnt+=1
print(cnt)
