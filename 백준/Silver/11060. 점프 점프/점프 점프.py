# 11060 백준 점프점프

n = int(input())  # n칸 짜리 미로
maze = list(map(int, input().split()))

d = [1e9] * n
d[0] = 0                           # 0번 인덱스부터 시작
for i in range(n):                 # 지금 현재 도달해 있는 거리
    for j in range(1, maze[i]+1):  # 지금 위치에서 뛸 수 있는 곳
        if i+j < n:                # 탈출 못했으면
            # 다른 경로로 i+j인덱스 도착한 경우 / 직전 위치에서 j만큼 뛴 경우
            d[i+j] =  min(d[i+j], d[i]+1)

# 프린트 구역
if d[n-1] == 1e9:
    print(-1)
else:
    print(d[-1])
