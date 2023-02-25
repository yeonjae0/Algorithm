N = int(input())

i_lst = []  # l값 넣어줌
# h_lst = []  # h값 넣어줌
lst = []
for _ in range(N):
    l, h = map(int, input().split())
    lst.append([l, h])
    i_lst.append(l)
    # h_lst.append(h)
height = [0] * (max(i_lst) + 1)

# height 해당하는 위치에 먼저 높이들 넣어 주기
for i in lst:
    height[i[0]] += i[1]
# 가장 높은 곳의 위치값 (인덱스값)
max_idx = height.index(max(height))

left = 0  # 왼쪽 포인터
right = len(height) - 1  # 오른쪽 포인터
left_num = 0  # 최신화 해줄 숫자

while left <= max_idx:
    if height[left] > left_num:
        left_num = height[left]
    else:
        height[left] = left_num
    left += 1

right_num = 0
while right > max_idx:
    if height[right] > right_num:
        right_num = height[right]
    else:
        height[right] = right_num
    right -= 1

print(sum(height))

