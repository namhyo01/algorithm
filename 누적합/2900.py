import sys
input = sys.stdin.readline

n,k = map(int, input().split())
X = list(map(int, input().split()))
maps = {}
for x in X:
    maps[x] = maps.get(x,0) + 1
Q = int(input())
a = [0 for _ in range(n+1)]
sums = [0 for _ in range(n+1)] # 누적합용

def something():
    global maps
    for k,v in maps.items():
        idx = 0
        while(idx < n):
            a[idx] += v
            idx += k
    for i in range(1,n+1):
        sums[i] = a[i - 1] + sums[i - 1]

something()
for _ in range(Q):
    L, R = map(int, input().split())
    print(sums[R+1] - sums[L])
