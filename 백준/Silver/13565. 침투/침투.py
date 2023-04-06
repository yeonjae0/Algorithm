# 13565 백준 침투
# 시간초과로 이번엔 시작점을 전부 넣어주고 시작

from collections import deque

dx = [-1, 1, 0, 0]  # 상하좌우
dy = [0, 0, -1, 1]




m, n = map(int, input().split())
arr = [list(map(int, input().lstrip())) for _ in range(m)]
cnt = 0
visited = [[0] * n for _ in range(m)]

q = deque()
for i in range(n):
    if arr[0][i] == 0:
        q.append((0, i))
while q:
    x, y = q.popleft()
    visited[x][y] = 1
    if x == m - 1:
        cnt += 1
        break
    for idx in range(4):
        nx, ny = x + dx[idx], y + dy[idx]
        if nx < 0 or nx >= m or ny < 0 or ny >= n or arr[nx][ny] == 1:
            continue
        if not arr[nx][ny] and visited[nx][ny] != 1:
            visited[nx][ny] = 1
            q.append((nx, ny))

if cnt == 1:
    print('YES')
else:
    print('NO')