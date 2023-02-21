def bfs(i, j):
    visited = [[0] * 16 for _ in range(16)]
    global graph
    global ans
    queue = []
    di = [-1, 1, 0, 0]  # 상하좌우
    dj = [0, 0, -1, 1]
    queue.append((i, j))
    visited[0][j] = 1

    while queue:
        i, j = queue.pop(0)
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]

            if (ni < 0) or (nj < 0) or (ni >= 16) or (nj >= 16):  # 범위 밖
                continue

            elif (graph[ni][nj] == 0) and (visited[ni][nj] == 0):  # 길을 찾아가는 중
                queue.append((ni, nj))
                visited[ni][nj] = 1

            if graph[ni][nj] == 3:  # 도착점 찾음
                ans = 1
                break


for t in range(1, 11):
    t = int(input())
    graph = [list(map(int, input())) for _ in range(16)]
    #print(graph)
    for i in range(16):
        for j in range(16):
            if graph[i][j] == 2:
                si, sj = i, j
    ans = 0
    bfs(si, sj)
    print(f'#{t} {ans}')