for tc in range(1, 11):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    arr_ = list(map(list, zip(*arr)))  # 전치
    rm_set = {0}
    for i in range(100):  # 전치 리스트에서 0 삭제
        arr_[i] = [x for x in arr_[i] if x not in rm_set]
    cnt = 0
    for lst in arr_:
        for idx in range(len(lst)-1):  # 12의 숫자 세기
            if lst[idx] == 1 and lst[idx+1] == 2:
                cnt += 1
    print(f'#{tc} {cnt}')