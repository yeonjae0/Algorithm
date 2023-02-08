t = int(input())
di = [0, 1, 0, -1]  # 오른쪽,아래,왼쪽,위
dj = [1, 0, -1, 0]

for a in range(1, t + 1):
    n = int(input())
    graph = []

    for _ in range(n):
        graph.append([0] * n)  # 각 칸에 우선 0 부여
# print(f'0이 채워진 그래프 {graph}')
# [i][j] i와 j의 값은 그냥 쭉 0 고정
    ni = 0
    nj = 0
    graph[ni][nj] = 1
    num = 1  # 0에 더해줄 숫자

    if n == 1:
        graph[ni][nj] = 1
        print(f'#{a}')
        print(graph[0][0])
        continue


    while True:
        if num < n:  # 초반 한 줄의  k값을 지정해주기 위한 조건문
            k = 0
        #print(k)
        ni += di[k]
        nj += dj[k]

        if (0 <= ni < n) and (0 <= nj < n) and (graph[ni][nj] == 0):
            num += 1
            graph[ni][nj] += num
            if num >= (n * n):
                break
        else:
            ni -= di[k]  # 범위에서 벗어나 else로 넘어왔기 때문에 다시
            nj -= dj[k]  # 위치를 바로 이전으로 초기화 시켜줘야함.
            k = (k + 1) % 4
    # 여긴 프린트
    print(f'#{a}')
    for z in graph:
        print(*z)