# 2805 백준 나무 자르기

import sys

n, m = map(int, sys.stdin.readline().split())  # n: 나무의 수, m: 필요한 나무 길이
tree_lst = list(map(int, sys.stdin.readline().split()))

s = 0
e = max(tree_lst)

rlt = 0  # 가장 작은 mid를 저장할 변수

while s <= e:
    mid = (s + e) // 2
    ans = 0  # 나무 합을 저장할 변수
    for tree in tree_lst:
        if tree > mid:
            ans += tree - mid
    # 나무가 적게 잘렸다
    if ans < m:
        e = mid - 1
    # 나무가 더 많이 혹은 알맞게 잘렸다
    else:
        rlt = mid
        s = mid + 1


print(rlt)
