N, M = map(int, input().split())
rectangle = [list(map(int, input().rstrip())) for _ in range(N)]
# print(rectangle)
standard = min(N, M)
ans = 0
for i in range(standard, 0, -1):  # 정사각형 변의 길이 -1
    for j in range(0, M-i+1):  # 가로 확인
        for k in range(0, N-i+1):  # 세로 확인
            if rectangle[k][j] == rectangle[k][j+i-1] == rectangle[k+i-1][j] == rectangle[k+i-1][j+i-1]:
                if ans < i * i:
                    ans = i * i
print(ans)