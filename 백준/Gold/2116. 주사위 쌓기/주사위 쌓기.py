def side(index):
    if index == (0, 5) or index == (5, 0):
        return [1, 2, 3, 4]
    elif index == (1, 4) or index == (4, 1):
        return [0, 2, 3, 5]
    else:
        return [0, 1, 4, 5]

# 주사위 개수 N
N = int(input())
dices = []
dices_extra = []
for _ in range(N):
    lst = list(map(int, input().split()))
    # dices.append(lst)
    lst[3], lst[4] = lst[4], lst[3]
    dices.append(lst)
    # dices_extra.append(lst)

max_candidates = []
sum_max = 0
for i in range(6):
    sum_max = 0
    # 첫 주사위 위 아래를 임의로 정해준다
    bottom = dices[0][i]
    top = dices[0][5-i]
    # 위 아래를 제외하고 될 수 있는 인덱스
    side_idx = side((i, 5-i))
    # 옆에서 올 수있는 가장 큰 수
    side_mx = max([dices[0][i] for i in side_idx])
    sum_max += side_mx
    next_bottom = top
    for j in range(1, N):
        # 다음 숫자의 바텀 인덱스
        bottom_idx = dices[j].index(next_bottom)
        # 다음 숫자의 바텀이 특정 숫자일 때 올 수 있는 옆면의 인덱스들
        side_idx = side((bottom_idx, 5 - bottom_idx))
        # 옆면 인덱스 중에 가장 큰 수
        side_mx = max([dices[j][i] for i in side_idx])
        sum_max += side_mx
        next_bottom = dices[j][5 - bottom_idx]
    max_candidates.append(sum_max)

print(max(max_candidates))