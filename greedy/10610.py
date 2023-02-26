import sys
input = sys.stdin.readline
n = input().strip()
data = []
sum = 0
for i in n:
    sum += int(i)
    data.append(i)

if '0' in data:
    if sum%3 != 0:
        print(-1)
    else:
        data.sort(reverse=True)
        print(''.join(data))
else:
    print(-1)
#30 60 90 120 150 180 210 240 270 300 330 360 390 420 450 480 510