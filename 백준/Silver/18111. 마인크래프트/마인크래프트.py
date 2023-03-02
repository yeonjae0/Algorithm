# n: 세로 / m: 가로 / b: 블럭의 개수
n, m, b = map(int, input().split())
arr = []
for _ in range(n):  # 1차원 리스트로 받기
    arr += map(int, input().split())

max_g = max(arr)
min_g = min(arr)

min_t = 1e9  # 최솟값을 갱신
ground = 0  # 최솟값일 때 땅의 높이
for height in range(min_g, max_g+1):
    t = 0  # 걸리는 시간
    block = b  # 블럭 초기화
    for i in range(n*m):
        if arr[i] > height:  # 블럭을 제거한다
            t += (arr[i] - height) * 2
            block += (arr[i] - height)
        elif arr[i] < height:  # 블럭을 쌓는다
            t += (height - arr[i])
            block -= (height - arr[i])

    if block >= 0 and min_t >= t:
        min_t = t
        ground = height

print(min_t, ground)