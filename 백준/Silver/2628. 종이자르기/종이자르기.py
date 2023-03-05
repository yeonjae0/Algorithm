w, h = map(int, input().split())
n = int(input())
x_lst = [0]  # 가로(세로로 잘리는 값)값을 넣어줄 리스트
y_lst = [0]  # 세로(가로로 잘리는 값)값을 넣어줄 리스트
ans = []
for _ in range(n):
    l, num = map(int, input().split())
    if l == 0:
        y_lst.append(num)
    else:
        x_lst.append(num)
x_lst.sort()  # 정렬해주고 마지막 값(범위) 어펜드
y_lst.sort()
x_lst.append(w)
y_lst.append(h)

for i in range(len(x_lst)-1):
    for j in range(len(y_lst)-1):
        area = (x_lst[i+1] - x_lst[i]) * (y_lst[j+1] - y_lst[j])
        ans.append(area)
print(max(ans))