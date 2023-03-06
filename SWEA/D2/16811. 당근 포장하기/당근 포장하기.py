
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    carrot = list(map(int, input().split()))

    carrot.sort()
    minV = 1000
    for i in range(0, N-2):
        for j in range(i+1, N-1):
            if carrot[i] != carrot[i+1] and carrot[j] != carrot[j+1]:
                A = i + 1
                B = j - i
                C = N - j - 1
                if A <= N//2 and B <= N//2 and C <= N//2:
                    if minV > max(A, B, C) - min(A,B,C):
                        minV = max(A, B, C) - min(A,B,C)
    if minV == 1000:  # 포장할 수 없는 경우
        minV = -1
    print(f'#{tc} {minV}')


