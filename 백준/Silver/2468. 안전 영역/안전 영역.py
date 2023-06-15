# 2468 백준 안전영역

from collections import deque

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
clone = [[0]*N for _ in range(N)]  # 침수지역 표시
vis = [[0]*N for _ in range(N)]
ans = []  # 안전지역 수
min_rain = 1e9
max_rain = 0

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 최소, 최대 강수량 확인
for i in range(N):
    for j in range(N):
        if arr[i][j] > max_rain:
            max_rain = arr[i][j]
        if arr[i][j] < min_rain:
            min_rain = arr[i][j]
lst = [ n for n in range(min_rain, max_rain + 1)]

# 강수량이 달라짐
for k in lst:  # k가 강수량
# 침수지역은 clone에 0->1로 변경
    for i in range(N):
        for j in range(N):
            if arr[i][j] < k:
                clone[i][j] = 1


# 일단 모든 구역을 돌면서 침수X, 방문X인 곳 찾아서 시작
    q = deque()
    cnt = 0
    for i in range(N):
        for j in range(N):
            if clone[i][j] == 0 and vis[i][j] == 0:
                q.append((i,j))
                cnt += 1
                while q:
                    x, y = q.popleft()
                    vis[x][y] = 1
                    for idx in range(4):
                        nx, ny = x + dx[idx], y + dy[idx]
                        if nx < 0 or ny < 0 or nx >= N or ny >= N or clone[nx][ny] == 1:
                            continue
                        if vis[nx][ny] != 1:
                            vis[nx][ny] = 1
                            q.append((nx,ny))
    ans.append(cnt)
    clone = [[0]*N for _ in range(N)]  # 침수지역 표시
    vis = [[0]*N for _ in range(N)]


print(max(ans))
