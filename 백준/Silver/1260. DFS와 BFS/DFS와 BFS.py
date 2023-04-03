def dfs(node):
    visited1[node] = 1
    print(node, end=' ')
    for j in range(1, n+1):
        if (visited1[j] == 0) and (graph[node][j] == 1):
            dfs(j)

# bfs는 큐 이용 (deque)
def bfs(node):
    q = []
    q.append(node)
    visited2[node] = 1
    while q:
        node = q.pop(0)
        print(node, end=' ')
        for i in range(1, n+1):
            if visited2[i] == 0 and graph[node][i] == 1:
                q.append(i)
                visited2[i] = 1


# 인풋 / 그래프 만들기
n, m, v = map(int, input().split())  # n: 정점의 개수 m: 간선의 개수 v: 탐색을 시작할 정점 번호
graph = [[0] * (n+1) for _ in range(n+1)]
visited1 = [0] * (n+1)
visited2 = [0] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1

# 함수 프린트
dfs(v)
print()
bfs(v)