# 23631 진심 좌우 반복뛰기
# 반복문 대신 등차수열 합 이용해볼까

import sys

tc = int(input())
for _ in range(tc):
    # n-1만큼 뛰고 멈춘다 / k만큼 달리는 거리 늘어남
    n, k = map(int, sys.stdin.readline().split())
    num = 0  # 뛰는 만큼 계속 더해줄 변수
    
    s, e = 0, 4472  # s, e, mid는 반복 횟수
    while s < e:
        my_sum = 0
        mid = (s + e) // 2
        my_sum = mid * k * (mid + 1) / 2  # 등차수열의 합
        if my_sum == n-1:
            break
        elif my_sum > n-1:
            e = mid
        else:
            s = mid + 1
    # print(mid, s, e, my_sum)
    # 마지막 반복 횟수 mid를 기준으로

    my_sum = mid * k * (mid + 1) / 2
    if my_sum > n-1:
        mid -= 1
        my_sum = mid * k * (mid + 1) / 2
    # print(f'{my_sum} my_sum')
    # print(f'{n-1-my_sum} n-1-my_sum')

    # s가 홀수면 L / 짝수면 R

    if mid % 2 == 0:
        ans = -(k * mid // 2) + (n-1-my_sum)
        print(f'{round(ans)} R')
    else:
        ans = k * (mid//2 +1) - (n-1-my_sum)
        print(f'{round(ans)} L')

        





