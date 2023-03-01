'''
ㄱ자 좌표를 버리고 나머지 좌표들을 1로 계산
좌표 하나가 넓이 1
'''
N = int(input())
area = set()
for i in range(N):
    x, y = map(int, input().split())
    for w in range(x, x+10):
        for h in range(y, y+10):
            area.add((w, h))
print(len(area))