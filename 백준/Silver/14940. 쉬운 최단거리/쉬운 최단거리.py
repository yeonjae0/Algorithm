def bfs(x, y):
    dx = [-1, 1, 0, 0]  # 상하좌우
    dy = [0, 0, -1, 1]
    q = []
    vis[x][y] = 1
    q.append((x,y))
    while q:
        x, y = q.pop(0)
        for idx in range(4):
            nx = x+dx[idx]
            ny = y+dy[idx]
            if 0 > nx or nx >= n or 0 > ny or ny >= m:
                continue
            if vis[nx][ny] == 1:
                continue
            if arr[nx][ny] == 1 and vis[nx][ny] == 0:
                clone[nx][ny] = clone[x][y] + 1
                q.append((nx, ny))
                vis[nx][ny] = 1


n, m = map(int, input().split())  # n: 세로 m: 가로
arr = [list(map(int, input().split())) for _ in range(n)]
vis = [[0]*m for _ in range(n)]
clone = [[0]*m for _ in range(n)]

# 스타트 지점
for i in range(n):
    for j in range(m):
        if arr[i][j] == 2:
            x, y = i, j

bfs(x, y)

# 갈 수 없는 곳 -1 출력
for i in range(n):
    for j in range(m):
        if clone[i][j] == 0 and arr[i][j] == 1:
            clone[i][j] = -1

# 정답 출력
for l in range(n):
    print(*clone[l])