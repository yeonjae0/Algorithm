N = int(input())
num_list = list(map(int, input().split()))
cnt = 1

cnt_list = []
if N == 1:
    cnt = 1
    cnt_list.append(cnt)

for i in range(len(num_list)-1):
    if num_list[i] <= num_list[i+1]:
        cnt += 1
        cnt_list.append(cnt)
    elif num_list[i] > num_list[i+1]:
        cnt = 1
cnt = 1
for j in range(len(num_list)-1):
    if num_list[j] >= num_list[j+1]:
        cnt += 1
        cnt_list.append(cnt)
    elif num_list[j] < num_list[j+1]:
        cnt = 1

print(max(cnt_list))