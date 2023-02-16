from bisect import bisect_left
import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))

data = []
for i in range(n):
    if len(data)==0 or data[-1] < A[i]:
        data.append(A[i])
        continue
    if data[-1] > A[i]:
        temp = bisect_left(data,A[i])
        data[temp] = A[i]
print(len(data))