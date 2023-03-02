T = int(input())
for tc in range(1, T+1):
    arr = [input() for _ in range(5)]

    cnt = 0
    for i in arr:
        if cnt < len(i):
            cnt = len(i)
    arr2 = []
    for st in arr:
        while len(st) != cnt:
            st += '*'
        arr2.append(st)

    arr_ = list(map(list, zip(*arr2)))
    ans = ''
    for st1 in arr_:
        for st2 in st1:
            if st2 != '*':
                ans += st2
                
    print(f'#{tc} {ans}')