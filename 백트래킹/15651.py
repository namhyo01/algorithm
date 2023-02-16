import sys
input = sys.stdin.readline

n,m = map(int, input().split())
data = [0 for _ in range(m)]
def backtracking(now):
    if now == m:
        for i in range(m):
            print(data[i],end=' ')
        print()
        return
    for i in range(n):
        data[now] = i+1
        backtracking(now+1)
backtracking(0)
