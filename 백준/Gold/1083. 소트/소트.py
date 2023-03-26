# 1083 백준 소트 (최최최쵳종)
import sys


n = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))
s = int(sys.stdin.readline())  # 교환 최대 횟수


for i in range(len(num)):
    tmp1 = len(num)
    # while s >= 0:
    while True:
        if i == num.index(max(num[i:tmp1])):
            break
        else:
            if num.index(max(num[i:tmp1])) - i <= s:
                s -= num.index(max(num[i:tmp1])) - i
                # for x in range(n-1, 0, -1):
                #     for y in range(0, x):
                #         if tmp1 == 0:
                #             break
                for y in range(num.index(max(num[i:tmp1]))-1, i-1, -1):
                    num[y+1], num[y] = num[y], num[y+1]
                    tmp1 -= 1
            else:
                tmp1 -= 1
print(*num)