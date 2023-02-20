lst = [int(input()) for _ in range(9)]
total = sum(lst)
n1 = n2 = 0
for i in range(9):
    for j in range(i+1, 9):
        tmp = 0
        tmp = total - lst[i] - lst[j]
        if tmp == 100:
            n1, n2 = lst[i], lst[j]
lst.remove(n1)
lst.remove(n2)
lst = sorted(lst)

for x in range(7):
    print(lst[x])
