import sys
N,S = map(int, sys.stdin.readline().split())
L = list(map(int,sys.stdin.readline().split()))
cnt = 0
def solve(idx, sums):
    global cnt
    global S,N
    global L
    if idx>= N:
        return
    sums += L[idx]
    if sums==S:
        cnt+=1
    solve(idx+1, sums) # 자기 자신을 포함
    solve(idx+1, sums-L[idx]) # 자기 자신은 제외
solve(0,0)
print(cnt)



