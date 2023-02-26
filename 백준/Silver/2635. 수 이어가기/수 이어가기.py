N = int(input())
ans = []  # 리스트를 담을 리스트

for i in range(1, N+1):
    lst = []  # 두번쨰 수에 따라 바뀔 리스트
    lst.append(N)
    lst.append(i)
    t = 0
    while True:
        tmp = lst[t] - lst[t+1]
        if tmp >= 0:
            lst.append(tmp)
            t += 1
        else:
            ans.append(lst)
            break
#print(ans)
max_len_ans = max(ans, key=len)
print(len(max_len_ans))
print(*max_len_ans)