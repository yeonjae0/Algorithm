n = int(input())
lst = []
for i in range(n):
    x = int(input())
    lst.append(x)
lst.sort()

for i in range(n):
    print(lst[i])