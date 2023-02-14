from bisect import bisect_left
import sys

input = sys.stdin.readline
n = int(input())
A = list(map(int,input().split()))
ans = []
for i in range(n):
    if len(ans)==0 or ans[-1] < A[i]:
        ans.append(A[i])
        continue
    if ans[-1] > A[i]:
        temp = bisect_left(ans,A[i])
        ans[temp] = A[i]
print(len(ans))