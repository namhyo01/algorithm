import sys
input = sys.stdin.readline
n = int(input())
answer = 0

chess = [0 for _ in range(n)]

def check(cnt):
    for i in range(cnt):
        if(chess[i]==chess[cnt] or abs(chess[i]-chess[cnt])==abs(cnt-i)):
            return False
    return True

def dfs(cnt):
    global answer
    if cnt==n:
        answer+=1
        return
    for i in range(n):
        chess[cnt] = i
        if(check(cnt)):
            dfs(cnt+1)
dfs(0)
print(answer)