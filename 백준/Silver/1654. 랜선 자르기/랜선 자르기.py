k, n = map(int, input().split())
lan_lst = [int(input()) for _ in range(k)]

s = 1
g = max(lan_lst)


while s <= g:
    mid = (s + g) // 2
    cnt = 0  # n과 같은 수인지 판단할 변수 (잘라지는 랜선 수)
    for lan in lan_lst:
        cnt += lan // mid
    if cnt >= n:  # 필요한 선보다 더 많이 잘렸으면
        s = mid + 1
    else:  # 잘린 선의 개수가 부족하다
        g = mid - 1

print(g)  # 최댓값