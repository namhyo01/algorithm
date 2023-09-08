import sys
input = sys.stdin.readline

s,e,q = input().split()
s = int(s[:2] + s[3:])
e = int(e[:2] + e[3:])
q = int(q[:2] + q[3:])

stu = {}
cnt = 0
while True:
    try:
        t, n = input().split()
        t = int(t[:2] + t[3:])
        if t<=s:
            stu[n] = stu.get(n, True)
        if e <= t <= q and stu.get(n, False):
            stu[n] = False
            cnt += 1
    except:
        break
print(cnt)