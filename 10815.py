import sys
input = sys.stdin.readline
n = int(input())
cardList = list(map(int, input().split()))
cardDict = {x:1 for x in cardList}
m = int(input())
checks = list(map(int, input().split()))
for i in checks:
    print(cardDict.get(i,0),end=' ')
