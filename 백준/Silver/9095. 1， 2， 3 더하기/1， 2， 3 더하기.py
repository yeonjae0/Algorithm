t = int(input())
for _ in range(t):
    n = int(input())
    d = [0] * (n + 1)
    d[1] = 1
    if n >= 2:
        d[2] = 2
    if n >= 3:
        d[3] = 4

    for i in range(4, n+1):
        d[i] = d[i-3] + d[i-2] + d[i-1]

    print(d[n])

#4를 구하는 식
# 1을 구하는 식에 3을 더해 만든다.
# 2를 구하는 식에 2를 더해 만든다.
# 3을 구하는 식에 1을 더해 만든다.
# 조합은 스택 개념 생각 이미 구현이 되어있다.