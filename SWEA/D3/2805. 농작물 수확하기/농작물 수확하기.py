T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().rstrip())) for _ in range(n)]
    ans = 0  # 수익을 넣어줄 변수
    for i in range(n):
        ans += arr[n//2][i]
    t = n//2 + 1  # 시작 지점 이동 
    for j in range((n-1)//2):
        t -= 1
        ans += sum(arr[n-1-j][t:t+j*2+1])
        ans += sum(arr[j][t:t+j*2+1])
    print(f'#{tc} {ans}')