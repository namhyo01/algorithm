import sys
from bisect import bisect_left
input=sys.stdin.readline

N,L = map(int, input().split())
h = list(map(int, input().split()))
h.sort()
for i in h:
    if L >= i:
        L += 1
    else:
        break

print(L)