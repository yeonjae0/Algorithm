# 17070 백준 파이프 옮기기 1
import sys

# 다시 재귀 사용 해봄
# 끝이 막히지 않았다는 말은 없음
def garo(r, c):
    global cnt
    if 0 <= c+1 <= n-1 and arr[n-1][n-1] != 1:
        if r == n-1 and c+1 == n-1:  # 가로로 도착
            cnt += 1
            return
        elif r+1 == n-1 and c+1 ==n-1 and arr[r+1][c] != 1 and arr[r][c+1] != 1:  # 대각으로 도착
            cnt += 1
            return
        elif 0 <= r+1 <= n-1 and arr[r][c+1] != 1 and arr[r+1][c] != 1 and arr[r+1][c+1] != 1:
            daegak(r+1, c+1)
        if arr[r][c+1] != 1:
            garo(r, c+1)
    return


def sero(r, c):
    global cnt
    if 0 <= r + 1 <= n - 1 and arr[n-1][n-1] != 1:
        if r+1 == n - 1 and c == n - 1:  # 세로로 도착
            cnt += 1
            return
        elif c+1 == n-1 and r+1 == n-1 and arr[r+1][c] != 1 and arr[r][c+1] != 1:  # 대각으로 도착
            cnt += 1
            return
        elif 0 <= c+1 <= n-1 and arr[r][c+1] != 1 and arr[r+1][c] != 1 and arr[r+1][c+1] != 1:
            daegak(r+1, c+1)
        if arr[r+1][c] != 1:
            sero(r+1, c)
    return

def daegak(r, c):
    global cnt
    # 대각 전부 범위 내
    if 0 <= r+1 <= n-1 and 0 <= c+1 <= n-1 and arr[n-1][n-1] != 1:
        if arr[r][c+1] != 1 and arr[r+1][c] != 1 and r + 1 == n-1 and c + 1 == n-1:
            cnt += 1
            return
        elif arr[r][c+1] != 1 and arr[r+1][c] != 1 and arr[r+1][c+1] != 1:
            daegak(r+1, c+1)
    # 세로 범위만 확인
    if 0 <= r+1 <= n-1 and arr[n-1][n-1] != 1:
        if r+1 == n-1 and c == n-1:
            cnt += 1
            return
        elif arr[r+1][c] != 1:
            sero(r+1, c)
    # 가로 범위만 확인
    if 0 <= c+1 <= n - 1 and arr[n-1][n-1] != 1:
        if r == n-1 and c+1 == n-1:
            cnt += 1
            return
        elif arr[r][c+1] != 1:
            garo(r, c+1)
    return

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
cnt = 0  # 마지막 지점에 도착하는 경우의 수 담아줄 변수
garo(0, 1)
print(cnt)