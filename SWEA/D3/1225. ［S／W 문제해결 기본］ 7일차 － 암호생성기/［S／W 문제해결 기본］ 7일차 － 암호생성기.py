for _ in range(10):
    t = int(input())
    lst = list(map(int, input().split()))

    while lst[-1] > 0:  # 뺀 숫자가 뒤로 들어가기 때문
        for j in range(1, 6):
            n = lst[0] - j  # pop 하기 전에 확인을 거치는 과정
            if n <= 0:  
                n = 0
                lst.pop(0)
                lst.append(0)
                break
            else:
                lst.append(lst.pop(0)-j)
    print(f'#{t}', end=" ")
    print(*lst)
