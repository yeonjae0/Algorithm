lst = []  # 경우의 수를 넣을 리스트

def dfs(x, y, num = ''):
    if len(num) == 6:
        if num not in lst:
            lst.append(num)
        return
    dx = [-1, 1, 0, 0]  # 상하좌우
    dy = [0, 0, -1, 1]

    for idx in range(4):
        nx = x + dx[idx]
        ny = y + dy[idx]
        if 0 > nx or nx >= 5 or 0 > ny or ny >= 5:
            continue
        else:
            dfs(nx, ny, num + arr[nx][ny])

arr = [input().split() for _ in range(5)]
for i in range(5):
    for j in range(5):
        dfs(i, j, arr[i][j])
print(len(lst))