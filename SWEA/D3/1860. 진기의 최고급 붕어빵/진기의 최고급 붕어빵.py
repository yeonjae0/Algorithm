T = int(input())
for tc in range(T):
    n, m, k = map(int, input().split())  # 손님 수 / m초 당 k개의 붕어빵
    res = list(map(int, input().split()))
    t = -1  # 시간(초)
    num = 0  # 현재 만들어져 있는 붕어빵 수
    while t < max(res):
        t += 1
        if t!= 0 and t % m == 0:
            num += k
        if t in res:
            if num > 0:
                num -= 1
            else:
                t = -10
                break
    if t == -10:
        print(f'#{tc+1} Impossible')
    else:
        print(f'#{tc+1} Possible')