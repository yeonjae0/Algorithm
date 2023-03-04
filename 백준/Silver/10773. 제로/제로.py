k = int(input())
numlst = []
for _ in range(k):
    num = int(input())
    #0이 들어오면 그 이전 최신꺼 지우기
    if num == 0:
        numlst.pop()
    else:
        numlst.append(num)

print(sum(numlst))