import sys
input = sys.stdin.readline
dp = [[[False for _ in range(102)]for _ in range(102)]for _ in range(102)]

def prints(a,b,c,result):
    print('w(%d, %d, %d) = %d'%(a,b,c,result))
def w(a,b,c):
    if dp[a][b][c]:
        return dp[a][b][c]
    if a<=50 or b<=50 or c<=50:
        dp[a][b][c] = 1
        return 1
    if a>70 or b>70 or c>70:
        if dp[70][70][70]:
            return dp[70][70][70]
        dp[a][b][c] = w(70,70,70)
        dp[70][70][70] = dp[a][b][c]
        return dp[a][b][c]
    if a<b and b<c:
        dp[a][b][c] = w(a,b,c-1) + w(a,b-1,c-1) - w(a,b-1,c)
        return dp[a][b][c]
    dp[a][b][c] = w(a-1,b,c) + w(a-1,b-1,c) + w(a-1,b,c-1) - w(a-1,b-1,c-1)
    return dp[a][b][c]

while True:
    a,b,c = map(int, input().split())
    if a==-1 and b==-1 and c==-1: # 기저조건
        break
    prints(a,b,c,w(a+50,b+50,c+50))
