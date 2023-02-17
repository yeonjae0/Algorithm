T = int(input())
for t in range(1, T+1):
    n, m = map(int, input().split())
    arr = []  # 배열 여기에 2차원으로 받기
    for _ in range(n):
        arr.append(list(map(int, input().split())))
    #print(arr)
    ans = []
    for i in range(n-m+1):  # 배열 세로
        for j in range(n-m+1):  # 배열 가로
            sum_m = 0
            for k in range(m):  # 파리채 세로
                for l in range(m):  # 파리채 가로
                    sum_m += arr[i+k][j+l]
            ans.append(sum_m)
    print(f'#{t} {max(ans)}')