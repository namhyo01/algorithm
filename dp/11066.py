import sys
input = sys.stdin.readline

t = int(input())


'''
    최솟값 결정은 마지막 합의 비용이 아닌 그 이전의 비용
'''
for _ in range(t):
    k = int(input())
    files = list(map(int, input().split()))
    dp = [[0] * (k) for _ in range(k)] # 메모이제이션 리스트
    for i in range(k-1):
        dp[i][i+1] = files[i] + files[i+1]
        for j in range(i+2, k):
            dp[i][j] = dp[i][j-1] + files[j] 
    print(dp)
    for i in range(2,k):
        for j in range(k-i):
            l = i+j
            temp = [dp[j][m] + dp[m+1][l] for m in range(j,l)]
            dp[j][l] += min(temp)
            print(dp)
    print(dp[0][k-1])

