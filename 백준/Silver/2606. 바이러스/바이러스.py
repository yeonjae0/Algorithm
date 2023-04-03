def bfs(s):
    global cnt
    visited = [0] * (V+1)
    visited[s] = 1
    q = [s]
    while q:
        node = q.pop(0)
        for i in arr[node]:
            if visited[i] == 0:
                q.append(i)
                visited[i] = 1
                cnt += 1
    return


V = int(input())
E = int(input())
arr = [[] for _ in range(V+1)]
cnt = 0
for _ in range(E):
    x, y = map(int, input().split())
    arr[x].append(y)
    arr[y].append(x)
bfs(1)
print(cnt)