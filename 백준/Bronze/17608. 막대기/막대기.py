n = int(input())
num = [int(input()) for _ in range(n)]
cnt = 1
top = num[-1]
for i in range(n-1, -1, -1):
    if num[i] > top:
        top = num[i]
        cnt += 1
print(cnt)