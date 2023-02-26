import sys
input = sys.stdin.readline
n = int(input())
A = []
for _ in range(n):
    name, a,b,c = input().split()
    A.append([name,int(a),int(b),int(c)])
A.sort(key=lambda x: (-x[1],x[2],-x[3],x[0]))
for a in A:
    print(a[0])