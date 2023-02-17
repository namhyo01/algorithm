import sys
from bisect import bisect_left
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))
A.sort()
m = int(input())
M = list(map(int, input().split()))
def bs(data,start,end):
    if start>end:
        return 0
    m = (start+end)//2
    if data == A[m]:
        return 1
    if data < A[m]:
        return bs(data, start, m-1)
    if data > A[m]:
        return bs(data,m+1,end)
for i in M:
    temp = bisect_left(A,i)
    if temp < n and A[temp] == i:
        print(1)
    else:
        print(0)


    # print(bs(i,0,n-1))

# A_dict = {x:1 for x in A}
# for i in M:
#     print(A_dict.get(i,0))