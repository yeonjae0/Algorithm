'''
왼쪽 아래를 기준으로 생각해보자
'''
s = set()

for _ in range(4):
    x1, y1, x2, y2 = map(int, input().split())

    for i in range(x1, x2):
        for j in range(y1, y2):
            s.add((i,j))
print(len(s))