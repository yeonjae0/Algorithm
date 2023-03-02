from itertools import combinations

N = int(input())

if N > 1022:
    print(-1)

else:
    combi_lst = []
    num = list(map(int, range(0, 10)))
    for i in range(1, 11):
        for j in combinations(num, i):
            tmp = sorted(list(j), reverse=True)
            combi_lst.append(int(''.join(map(str, tmp))))
        combi_lst.sort()

    print(combi_lst[N])