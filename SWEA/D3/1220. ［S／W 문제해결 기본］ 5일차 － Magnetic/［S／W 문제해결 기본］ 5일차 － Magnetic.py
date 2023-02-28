T = 10
for tc in range(1, T + 1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(100)]
    board_col = list(map(list, zip(*board)))
    cnt = 0
    # 삭제할 원소 집합 생성
    for lst in board_col:
        while 0 in lst:
            lst.remove(0)
 
    # 앞에서부터 1 빼기
    for lst in board_col:
        i = 0
        while lst[i] == 2:
            lst.pop(0)
 
    # 뒤에서부터 2 빼기
    for lst in board_col:
        while lst[-1] == 1:
            lst.pop(-1)
 
    # stack = []
    for lst in board_col:
        for i in range(1, len(lst)):
            if lst[i] == 1 and lst[i-1] == 2:
                cnt += 1
 
    print(f'#{tc}', cnt + 100)