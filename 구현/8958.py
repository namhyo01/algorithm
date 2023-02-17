import sys
input = sys.stdin.readline
T = int(input())

def solve(string):
    add = 0
    ans = 0
    for i in string:
        if i=='O':
            add += 1
            ans += add
        else:
            add = 0
    return ans
for _ in range(T):
    quiz = input()
    print(solve(quiz))
