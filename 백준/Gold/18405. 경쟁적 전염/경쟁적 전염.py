from collections import deque


N, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
S, X, Y = map(int, input().split())
lst = []

for i in range(N):
    for j in range(N):
        if arr[i][j] != 0:
            lst.append((arr[i][j], 0, i, j))

lst.sort()
q = deque(lst)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while q:
    virus, s, x, y = q.popleft()
    if s == S:
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if (0 <= nx) and (nx < N) and (0 <= ny) and (ny < N):
            if arr[nx][ny] == 0:
                arr[nx][ny] = virus
                q.append((virus, s+1, nx, ny))

print(arr[X-1][Y-1])