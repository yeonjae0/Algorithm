T = int(input())
for test_case in range(1, T+1):
    cnt = 0  # 잘릴 수 있는 쇠막대기의 수
    st = input()
    ans = 0  # 이미 잘린 막대기 수
    for i in range(len(st)):  # 막대기 시작 또는 레이저
        if st[i] == '(':  # 기본적으로 '('를 막대기 시작이라고 생각
            cnt += 1  # 레이저여도 일단 더해주기 (나중에 바로 빼줄거임)
        else:   # ')' 바로 앞의기호를 검사
            if st[i-1] == '(':  # 레이저일 경우
                cnt -= 1  # 레이저면 먼저 빼주기
                ans += cnt
            else:  # 막대기의 끝
                cnt -= 1  # 쇠막대기 하나 없어지니까
                ans += 1  # 잘리고 남은 덩어리 하나
    print(f'#{test_case} {ans}')
