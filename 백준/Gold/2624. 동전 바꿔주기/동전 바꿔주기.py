# 2624 백준 동전 바꿔주기
# DP

t = int(input())  # 지폐의 금약
k = int(input())  # 동전의 가지 수


lst =[[0,0]]
for _ in range(k):
    a, b = map(int, input().split())
    lst.append([a, b])
lst.sort()  # lst: [[금액, 가지수], [], [] ...]

# d의 1번 인덱스에는 첫 번째 동전 경우의 수 해당 리스트의 자릿수는 금액만큼
d = [[0] * (t+1) for _ in range(k+1) ]
d[0][0] = 1  # 0원을 넣는 경우 / 시작점

for i in range(1, k+1):  # 동전의 가지 수를 돈다 1~
    for j in range(t+1):  # 지페의 금액
        d[i][j] = d[i-1][j]  # 이전 동전에서의 값을 받아온다
        for k in range(1, lst[i][1] + 1):  # 해당 코인의 개수를 돈다(i 번째 코인)
            if j-k*lst[i][0] >= 0:  # 지금 도는 금액(j)에서 금액*동전 뺀 금액이 0보다 크면
                d[i][j] += d[i-1][j-k*lst[i][0]]
            else:
                break
print(d[-1][-1])