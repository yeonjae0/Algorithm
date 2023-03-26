# 6236 용돈 관리

import sys

# n: n일 / m: 통장에서 돈을 꺼낼 횟수 
n, m = map(int, sys.stdin.readline().split())

payment = [int(sys.stdin.readline()) for _ in range(n)]

# s = 1
# e = 10000
s = max(payment)
e = sum(payment)
cnt = 1
# ans = 10001
while s <= e:
    mid = (s + e) // 2
    pocket = mid  # 현재 가지고 있는 돈
    cnt = 1  # m과 비교할 변수 (통장에서 돈 꺼냄)
    for money in payment:
        # 주머니에 지불할 돈이 있다
        if money <= pocket:
            pocket -= money
        # 지불 금액이 더 크다
        else:
            # # 애초에 지불을 못할 금액이었다
            # if mid < money:
            #     s = mid + 1
            #     break
            pocket = mid
            cnt += 1
            pocket -= money
        # 인출 횟수 너무 많음
    if cnt > m:
        s = mid + 1
    else:
        # 값 저장
        ans = mid
        e = mid - 1

print(mid)
    
