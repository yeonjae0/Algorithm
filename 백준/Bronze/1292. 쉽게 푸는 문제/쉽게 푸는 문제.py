a, b = map(int, input().split())
cnt = 0
t = 1
lst = []
while True:
    for _ in range(t):
        lst.append(t)
        cnt += 1
    t += 1
    if cnt > b:
        break
print(sum(lst[a-1:b]))