# 2470 백준 두 용액

import sys

import heapq

heap = []

n = int(input())
lst = list(map(int, sys.stdin.readline().split()))
# 힙 안에 넣어주기
for i in lst:
    heapq.heappush(heap, [abs(i),i])
# print(heap)

num = []  # 이전의 수를 기억 하기 위한 리스트
num.append(heapq.heappop(heap)[1])
result = 10000000000
for j in range(len(heap)):
    a, b = heapq.heappop(heap)
    tmp = num[-1] + b
    if abs(tmp) < result:
        result = abs(tmp)
        ans = [num[-1], b]
    # num.pop()
    num.append(b)
ans.sort()
print(*ans)