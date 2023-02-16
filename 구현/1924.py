import sys

weekend = ['SUN','MON','TUE','WED','THU','FRI','SAT']
days = [31,28,31,30,31,30,31,31,30,31,30,31]


input = sys.stdin.readline
x,y = map(int, input().split())
month = day = 1
while True:
    if month == x:
        break
    day += days[month-1]
    month+=1
day+=y-1
print(weekend[day%7])

