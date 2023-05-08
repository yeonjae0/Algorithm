
from itertools import combinations
from collections import deque
'''
조합을 구하기
구한 조합을 BFS 함수로 넘기기
bfs => 상하좌우
2의 위치를 전부 deque에 넣고 돌리기
돌린 후 0의 수 세기
'''
def bfs(t):
    global ans

    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]
    clone = [[0] * m for _ in range(n)]

    d = deque()
    cnt = 0

    for i in range(n):
        for j in range(m):
            if arr[i][j] == 2:
                d.append((i,j))
                clone[i][j] = 2
            elif arr[i][j] == 1:
                clone[i][j] = 1
    for x, y in t:
        clone[x][y] = 1

    while d:
        i, j = d.pop()
        for idx in range(4):
            nx = i + di[idx]
            ny = j + dj[idx]
            if 0 <= nx < n and 0 <= ny < m and clone[nx][ny] == 0:
                d.append((nx, ny))
                clone[nx][ny] = 2

    for i in range(n):
        for j in range(m):
            if clone[i][j] == 0:
                cnt += 1

    if cnt > ans:
        ans = cnt
    return ans


n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
empty = []
ans = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            empty.append((i,j))
combi = list(combinations(empty, 3))

for t in combi:
    bfs(t)

print(ans)


