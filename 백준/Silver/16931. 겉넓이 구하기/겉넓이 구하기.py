N, M = map(int, input().split())
arr = [list(map(int, input().split())) for x in range(N)]
arrzip = list(zip(*arr))
# print(arr)
# print(arrzip)

ans = N * M  # (윗면, 아랫면)
# 반복문 돌면서 사이드 겉넓이
# 그 다음 블럭이 앞의 블럭보다 크다면 그만큼 겉넓이 늘어남
for i in range(N):  # 줄
    for a in range(M):
        if a == 0:
            ans += arr[i][a]
        else:
            if arr[i][a] > arr[i][a-1]:
                ans += arr[i][a] - arr[i][a-1]
                
for i in range(M):
    for c in range(N):
        if c == 0:
            ans += arrzip[i][c]
        else:
            if arrzip[i][c] > arrzip[i][c-1]:
                ans += (arrzip[i][c] - arrzip[i][c-1])

    # for b in range(M-1, 0, -1):
    #     if b == M-1:
    #         ans += arr[i][b]
    #     if arr[i][b] < arr[i][b-1]:
    #         ans += (arr[i][b-1] - arr[i][b])
    #
    # for d in range(N-1, 0, 0--1):
    #     if d == N-1:
    #         ans += arrzip[i][d]
    #     if arrzip[i][d] < arrzip[i][d-1]:
    #         ans += (arrzip[i][d-1] - arrzip[i][d])
ans = ans * 2
print(ans)