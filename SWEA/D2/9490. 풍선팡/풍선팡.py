T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    sum_lst = []
    di = [-1, 1, 0, 0]  # 상하좌우
    dj = [0, 0, -1, 1]
    for i in range(n):
        for j in range(m):
            rlt = arr[i][j]  # 가운데 꽃가루
            t = arr[i][j]
            for k in range(4):  # 방향
                for mul in range(1, t+1):
                    ni = i + di[k] * mul
                    nj = j + dj[k] * mul
                    if 0 <= ni < n and 0 <= nj < m:
                        rlt += arr[ni][nj]
            sum_lst.append(rlt)

    print(f'#{tc} {max(sum_lst)}')