# 기둥의 개수 N (1<=N<=1000)
N = int(input())
lst = [0] * 1001
mx_height = mx_idx = 0 # 가장 높은 기둥이 나오는 인덱스
for _ in range(N):
    # 왼쪽 면의 위치 L, 높이 H (1<= _ <=1000)
    L, H = map(int, input().split())
    lst[L] = H
    mx_height = max(mx_height, H)
mx_idx = lst.index(mx_height)

# 첫번째 나오는 가장 큰 기둥을 기준으로 두 구간으로 나누기
lst_a = lst[:mx_idx + 1]
lst_b = lst[mx_idx:]

# 왼쪽에서 빛 쐈을 때
current_height = lst_a[0]
area = 0
for i in range(1, len(lst_a)):
   # 앞은 0이었고 더 높은 기둥을 만났을 경우 (처음 시작할 때)
    if current_height == 0 and lst_a[i] >= current_height:
        # 높이 갱신
        current_height = lst_a[i]
        # 넓이에 더하기
        area += current_height
    # 0을 지나서 기둥 갱신되었는데 또 더 높은 기둥 만난 경우
    elif current_height != 0 and lst_a[i] >= current_height:
        # 더 높은 기둥으로 높이 갱신
        current_height = lst_a[i]
        # 넓이에 더하기
        area += current_height
    # 이전 기둥이 0이 아니었는데 중간에 0을 만난 경우 (오목하게 들어간 경우)
    elif current_height != 0 and lst_a[i] == 0:
        # 오목한 부분 상관없이 지금 가지고 있는 높이 더하기
        area += current_height
    # 이전 기둥 0이 아니었고 더 작은 기둥 만난 경우
    elif current_height != 0 and lst_a[i] < current_height:
        # 갱신 안하고 넓이에 더하기
        area += current_height
    else:
        pass

current_height = lst_b[-1]
for i in range(len(lst_b) - 1, -1, -1):
    # 저장된 높이보다 높으면
    if current_height == 0 and lst_b[i] >= current_height:
        current_height = lst_b[i]
        area += current_height
    elif current_height != 0 and lst_b[i] >= current_height:
        current_height = lst_b[i]
        area += current_height
    elif current_height != 0 and lst_b[i] == 0:
        area += current_height
    elif current_height != 0 and lst_b[i] < current_height:
        area += current_height
    else:
        pass

print(area - mx_height)