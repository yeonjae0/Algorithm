n = int(input())
stairs = [int(input()) for _ in range(n)]
#print(stairs)
d = [0] * n  # 각 인덱스번째 계단에 최댓값 저장 (0부터 시작)
d[0] = stairs[0]
for j in range(1, 3):
    if (n >= 2) and (j == 1):
        d[1] = d[0] + stairs[1]
    if (n >= 3) and (j == 2):
        d[2] = max(d[0] + stairs[2], stairs[1] + stairs[2])

for i in range(3, n):
# 1번)이전 계단을 밟는 경우: 2칸 뛰기+ 전계단+지금 계단
# 2번)이전 계단을 건너뛴 경우: 전전 계단 + 지금 계단
    d[i] = max(d[i-3]+stairs[i]+stairs[i-1], d[i-2]+stairs[i])

print(d[-1])