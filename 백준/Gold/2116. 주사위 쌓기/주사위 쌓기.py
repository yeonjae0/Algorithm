# 2116 백준 주사위 쌓기

dic = {0: 5, 1: 3, 2: 4, 3: 1, 4: 2, 5: 0}


def bot_to_top(llst, bot_num):
    # 리스트 내에서 아래 숫자를 찾고 해당하는 위치 파악 후
    # 다음 탑 숫자를 반환
    global next_top
    for i in range(len(llst)):
        if llst[i] == bot_num:
            next_top = llst[dic[i]]

            
def dice_idx_max(lst, num):
    # top 숫자를 1차원 리스트 lst에서 찾아서 해당 리스트 내의 인덱스를 찾고
    # (0, 5), (1, 3), (2,4) 묶어서 제외한 후 나머지 중에 최대를 반환
    for k in lst:
        if k == num:
            if lst.index(k) in (0, 5):
                tmp_lst = [lst[1], lst[2], lst[3], lst[4]]

            elif lst.index(k) in (1, 3):
                tmp_lst = [lst[2], lst[0], lst[4], lst[5]]
            else:
                tmp_lst = [lst[0], lst[1], lst[3], lst[5]]
    #print(tmp_lst)
    m_num = max(tmp_lst)
    return m_num



N = int(input())
dice = [list(map(int, input().split())) for _ in range(N)]
#print(dice)
# tmp_ans = 0 #최대를 계속 더해줌
ans = []  # 최댓값의 합들을 보관
next_top = 0  # 윗면에 올 숫자

for i in dice[0]:  # 첫 주사위 돌 때 위에 오는 수
    next_top = i
    tmp_ans = 0
    # i는 다음 주사위 아래 숫자와 같고 next_top은 다음 주사위 위에 있을 숫자
    for j in range(0, N):  # N개의 주사위를 돈다
        #print(dice_idx_max(dice[j], next_top))
        tmp_ans += dice_idx_max(dice[j], next_top)
        bot_to_top(dice[j], next_top)

    ans.append(tmp_ans)

print(max(ans))
