import sys
input = sys.stdin.readline
n,m,k = map(int, input().split())
teams = 0
while n >= 2 and m >= 1 and n + m >= k + 3:
    n -= 2	
    m -= 1	
    teams += 1	
print(teams)