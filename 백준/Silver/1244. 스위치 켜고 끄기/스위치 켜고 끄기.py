total_switch = int(input())
s_lst = list(map(int, input().split()))
s_lst.insert(0, 5)
student = int(input())

for _ in range(student):
    s, num = map(int, input().split())
    if s == 1:  # 남학생일 때 배수
        for j in range(1, total_switch+1):
            if j % num == 0:
                if s_lst[j] == 0:
                    s_lst[j] = 1
                else:
                    s_lst[j] = 0
    else:  # 여학생일 때
        i = 0
        if s_lst[num] == 0:  # 우선 num 인덱스 바꿔주기
            s_lst[num] = 1
        else:
            s_lst[num] = 0

        while True:
            i += 1
            if(1 <= num-i < total_switch+1) and (1 <= num+i < total_switch+1) and (s_lst[num-i] == s_lst[num+i]):

                if s_lst[num-i] == 0:
                    s_lst[num-i] = 1
                else:
                    s_lst[num-i] = 0
                if s_lst[num+i] == 0:
                    s_lst[num+i] = 1
                else:
                    s_lst[num+i] = 0
            else:
                break
s_lst.pop(0)
if total_switch <= 20:
    print(*s_lst)
else:
    for l in range(total_switch//20):
        print(*s_lst[l * 20 : (l+1)*20])
    print(*s_lst[total_switch//20*20: total_switch])