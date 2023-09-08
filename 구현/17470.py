import sys
from copy import deepcopy
input = sys.stdin.readline

n,m,r = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(n)]
temp_A = [[[0 for _ in range(m//2)] for _ in range(n//2)] for _ in range(4)]
op = list(map(int, input().split()))
for i in range(n//2):
    for j in range(m//2):
        temp_A[0][i][j] = A[i][j]
for i in range(n//2):
    for j in range(m//2,m):
        temp_A[1][i][j-m//2] = A[i][j]
for i in range(n//2,n):
    for j in range(m//2):
        temp_A[2][i-n//2][j] = A[i][j]

for i in range(n//2,n):
    for j in range(m//2,m):
        temp_A[3][i-n//2][j-m//2] = A[i][j]

def cal1(): # 상하 반전
    global res, sample_list
    if res[2] % 2: # 회전이 되어있다면 상하반전이 좌우반전이 되기에
        res[1] = not res[1]
    else:
        res[0] = not res[0]
    sample_list[0], sample_list[1] = sample_list[1], sample_list[0]
def cal2(): # 좌우 반전
    global res, sample_list
    if res[2] % 2: # 회전이 되어있다면 상하반전이 좌우반전이 되기에
        res[0] = not res[0]
    else:
        res[1] = not res[1]
    sample_list[0][1], sample_list[0][0] = sample_list[0][0], sample_list[0][1]
    sample_list[1][1], sample_list[1][0] = sample_list[1][0], sample_list[1][1]
    pass
def cal3(): # 오른쪽 90
    '''
    n*m 행렬에서
    i,j -> m*n의  j,n-1-i에 위치
    '''
    global res
    res[2] = (res[2] + 1) % 4 
    cal5()
    # global A
    # maps = [[A[n-1-i][j] for i in range(n)] for j in range(m)]
    # A = maps
def cal4(): # 왼쪽 90
    global res
    res[2] = (res[2] - 1) % 4
    cal6()
    # global A
    # maps = [[A[i][m-1-j] for i in range(n)] for j in range(m)]
    # A = maps
def cal5(): # 부분배열 1번을 2번, 2번을 3번 3번을 4번 4번을 1번 => 우회전이네?
    global sample_list
    new = [[0,0],[0,0]]
    new[0][0] = sample_list[1][0]
    new[0][1] = sample_list[0][0]
    new[1][0] = sample_list[1][1]
    new[1][1] = sample_list[0][1]
    sample_list = deepcopy(new)
    pass
def cal6(): # 부분 배열 1번을 4번, 4번을 3번, 3번을 2번, 2번을 1번
    global sample_list
    new = [[0,0],[0,0]]
    new[0][0] = sample_list[0][1]
    new[0][1] = sample_list[1][1]
    new[1][0] = sample_list[0][0]
    new[1][1] = sample_list[1][0]
    sample_list = deepcopy(new)
    pass
sample_list = [[0,1], [2,3]] # 전체 배열을 돌리지 않는다.
func_list = [cal1, cal2,cal3,cal4,cal5,cal6]
res = [False, False, 0] # 상하 반전, 좌우 반전, 회전 방향

for i in op:
    func_list[i-1]()

def turn(arr):
    # new_arr = [[0 for _ in range(len(arr))] for _ in range(len(arr[0]))]

    # for i in range(len(arr[0])):
    #     for j in range(len(arr)):
    #         new_arr[i][j] = arr[len(arr) - j - 1][i]

    # return new_arr
    maps = [[arr[len(arr)-1-i][j] for i in range(len(arr))] for j in range(len(arr[0]))]
    return maps
    # for i in range(len(arr[0])):
        # for j in range(len(arr)):
if res[0]:
    for i in range(4):
        temp_A[i].reverse()
if res[1]:
    for i in range(4):
        for j in range(len(temp_A[i])):
            temp_A[i][j].reverse()

for _ in range(res[2]):
    for i in range(4):
        temp_A[i] = turn(temp_A[i])

ans = []
ans.extend(deepcopy(temp_A[sample_list[0][0]]))
ans.extend(deepcopy(temp_A[sample_list[1][0]]))

for i in range(len(ans)//2):
    ans[i].extend(temp_A[sample_list[0][1]][i])
    ans[len(ans) // 2 + i].extend(temp_A[sample_list[1][1]][i])
for i in ans:
    print(*i)
