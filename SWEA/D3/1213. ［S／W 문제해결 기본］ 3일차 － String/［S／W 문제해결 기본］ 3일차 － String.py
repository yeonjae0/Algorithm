for t in range(1, 11):
    tc = int(input())
    st = input()
    case = input() #전체 문자열
    i = 0
    cnt = 0
    while i <= len(case)-1:
        if case[i:i+len(st)] == st:
            cnt +=1
        i += 1
    print(f'#{tc} {cnt}')