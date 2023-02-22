def in_order(n):
    if n:
        in_order(int(data[n][2]))
        print(data[n][1], end='')
        in_order(int(data[n][3]))

for t in range(1, 11):
    N = int(input())
    data = [input().split() for _ in range(N)]

    data.insert(0,[0, 0, 0, 0])

    for i in data:
        # 자식이 없거나 하나인 경우, 크기를 맞추자
        while len(i) != 4:
            i.append('0')
    # print(data)
    print(f'#{t}', end=' ')
    in_order(1)  # 루트 정점 번호는 항상 1(문제)
    print()