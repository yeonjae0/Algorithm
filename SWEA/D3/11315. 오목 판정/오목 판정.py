def omok(arr):
    dx = [-1, 0, 1, 1]
    dy = [1, 1, 1, 0]
    cnt = 0
    for x in range(n):
        for y in range(n):
            for idx in range(4):
                cnt = 0
                for mul in range(5):  # 총 5번까지 간 방향에 대해 탐색
                    nx = x + dx[idx] * mul
                    ny = y + dy[idx] * mul
                    if (0 <= nx < n) and (0 <= ny < n) and (arr[nx][ny] == 'o'):
                        cnt += 1
                        if cnt == 5:
                            return True
                    else:
                        break
    if cnt != 5:
        return False

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = [input() for _ in range(n)]
    if omok(arr):
        print(f'#{tc} YES')
    else:
        print(f'#{tc} NO')