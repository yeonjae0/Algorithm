w, h =map(int, input().split())
x, y =map(int, input().split())
t = int(input())


'''
ex)
w = 6
rrllllllrrrrrrllllllrrr...
rr (rrrrrr llllll) lll
'''
delta = [1, -1]
k = 0  # delta의 인덱스

# x좌표를 구해보자
x_t = t % (2 * w)
while x_t != 0:
    if 0 <= x+delta[k] <= w:
        x += delta[k]
        x_t -= 1
    else:
        k = (k+1) % 2

# y좌표를 구해보자
k = 0  # k 초기화
y_t = t % (2 * h)
while y_t != 0:
    if 0 <= y+delta[k] <= h:
        y += delta[k]
        y_t -= 1
    else:
        k = (k+1) % 2
print(x, y)