# 뒤부터 확인
T = int(input())
for t in range(1, T +1):
    n = int(input())
    # 리스트를 뒤집어서 받는다.
    lst = list(map(int, input().split()))[::-1]
    #print(lst)

    mx = ans = 0

# 최댓값보다 요소가 작으면 차액이 바로 ans에 저장
    for i in lst:
        if mx > i:
            ans += (mx -i)
            # 최댓값이 요소보다 작으면 최댓값 갱신 처음에는 무조건 갱신됨
        else:
            mx = i
    print(f'#{t} {ans}')