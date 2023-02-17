import sys
input = sys.stdin.readline
T = int(input())
P = [0 for _ in range(101)]
P[1] = P[2] = P[3] = 1
P[4] = P[5] = 2
P[6] = 3
P[7] = 4
P[8] = 5
P[9] = 7
P[10] = 9

for i in range(11,101):
    P[i] = P[i-2] + P[i-3]
for _ in range(T):
    n = int(input())
    print(P[n])