# 1493 백준 박스 채우기

L, W, H = map(int, input().split())
n = int(input())
boxes = []
# 박스 리스트에 변의 길이, 개수 넣어줌
for i in range(n):
    a, b = map(int, input().split())
    boxes.append([2**(a), b])
boxes.sort(reverse=True)
total = L*H*W
my_total = 0  # 답이 맞는지 확인할 부피
ans = 0  # 총 사용할 상자 개수
used_box = 0  # 사용한 박스
my_cnt = 0  # 현재 시점에서의 박스 사용 개수
used_box_total = 0
idx = 1

# 여기서부터 시작
for i in range(len(boxes)):
#     if i == len(boxes)-1 or boxes[i+1][0] == 0:  # 인풋 연속성이 없을 경우 대비
#         idx = 1
#     else:
#         idx = boxes[i][0] - boxes[i+1][0]

    used_box_total *= 2 ** (idx * 3)
    side, box_cnt = boxes[i]
    box = (L//side) * (W//side) * (H//side)  # 빈 상자에 최대로 넣을 수 있는 개수
    tmp = box - used_box_total
    used_box = min(tmp, box_cnt)  # 현재 사용하는 상자!
    # used_box_total += used_box * (2 ** (idx * 3))
    used_box_total += used_box
    my_total += used_box * (side ** 3)  # 채워진 부피
    ans += used_box
    if my_total == total:
        break

if my_total == total:
    print(ans)
else:
    print(-1)