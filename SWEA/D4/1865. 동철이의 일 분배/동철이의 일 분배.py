

def backtracking(depth, val):
    global max_v
    if val <= max_v:  # 아래로 내려갈수록 수는 무조건 작아짐
        return
    if depth == n: # 깊이가 최대면 탐색 종료
        if val > max_v:  # 끝까지 도달하면 max_v값으로 넣어준다
            max_v = val
        return
    for i in range(n):
        if visited[i] == 0:
            visited[i] = 1
            backtracking(depth+1, val*arr[depth][i] / 100)
            visited[i] = 0


T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    max_v = 0  # 최댓값을 넣어줄 변수
    visited = [0] * n
    backtracking(0, 1)
    print(f'#{tc} {format(max_v*100, ".6f")}')


