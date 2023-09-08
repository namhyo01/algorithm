import sys
input = sys.stdin.readline

G = int(input())
p = int(input())
g = []
for _ in range(p): g.append(int(input()))

parent = [i for i in range(G+1)]

# 싹다 루트로 보내는게 정배

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a,b):
    a = find(a)
    b = find(b)
    parent[max(a,b)] = min(a,b)

cnt = 0
for i in g:
    root = find(i)
    if root == 0:
        break
    union(root, root-1)
    cnt += 1
print(cnt)
