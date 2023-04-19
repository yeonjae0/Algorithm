# 1493 백준 센서

n = int(input())  # 센서의 개수
k = int(input())  # 집중국의 개수
lst = list(map(int, input().split()))
ans = 0
lst.sort()
# print(lst)
gap = []  # 각 구간 별 거리 차이 넣어줄 리스트
if n <= k:  # 집중국의 수가 더 많을 경우
    print(0)
else:
    for i in range(1, len(lst)):  # 거리 차이 구하기
        gap.append(lst[i]-lst[i-1])
    # print(gap)

    for i in range(k-1):
        gap.remove(max(gap))

    print(sum(gap))
