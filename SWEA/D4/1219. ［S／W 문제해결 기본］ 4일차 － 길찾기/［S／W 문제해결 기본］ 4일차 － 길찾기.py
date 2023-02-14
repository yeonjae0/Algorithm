def dfs(s, g):
    if s == g:
        lst.append(99)
        return
    visited[s] = 1
    lst.append(s)
    for k in range(100):
        if arr[s][k] == 1 and visited[k] == 0:
            dfs(k, g)

for t in range(1, 11):
    V, E = map(int, input().split())
    num = list(map(int, input().split()))  #숫자들 받기
    arr = [[0] * 101 for _ in range(101)]  # 연결을 확인할 2차원 리스트
    for i in range(E):
        n1, n2 = num[i * 2], num[i * 2 + 1]
        arr[n1][n2] = 1  # n1과 n2 연결
    visited = [0] * 100
    lst = []
    dfs(0, 99)
    #print(lst)

    if 99 in lst:
        print(f'#{t} 1')
    else:
        print(f'#{t} 0')