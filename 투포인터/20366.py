import sys
input = sys.stdin.readline

n = int(input())
h = list(map(int, input().split()))
h.sort()
ans = sys.maxsize
for i in range(n):
    for j in range(i+3, n):
        l, r = i+1, j-1
        while l < r:
            height = h[i] + h[j] - (h[l] + h[r])
            ans = min(ans, abs(height))
            if height < 0: r -= 1 # l의 값이 너무 큰거 같으니 r을 줄인다
            else: l += 1
print(ans)