import sys
input = sys.stdin.readline

'''
    1. i,j가 n보다 작다면 j+1 or i+1로만 이동
    2. i=n, j가 n보다 작다면 j+1로만 => 당연
    3. 역도 i+1만 ㄱ
    4. i = j= n이면 출구
    a,b에서 c,d로 갈려면 A[a][b] > A[c][d]가 되어야 한다
        그러나 각 원소에 버튼이 있어 누르면 해당 원소값이 1증가
            하지만 돈이 든다 돈을 최소화해보자
'''

n = int(input())
A = [list(map(int, input().split())) for _ in range(n)]
# print(A)
dp = [[0 for _ in range(n)] for _ in range(n)] # 모든 지역을 다 탐색하긴 해야할듯 하니 dp

for i in range(n): # 행 탐색
    for j in range(n):
        if i<=0 and j<=0: continue # 이러면 넘어가자
        bi = bj = sys.maxsize
        if i >= 1:
            bi = dp[i-1][j] + (0 if A[i][j] < A[i-1][j] else A[i][j] - A[i-1][j] + 1) 
        if j >= 1:
            bj = dp[i][j-1] + (0 if A[i][j] < A[i][j-1] else A[i][j] - A[i][j-1] + 1)
        dp[i][j] = min(bi,bj)
print(dp[n-1][n-1])

