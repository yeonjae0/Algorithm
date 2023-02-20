n = int(input())
n_list = list(map(int, input().split()))
#가장 작은 값을 먼저 곱해주는게 최소 비용
price = 0
n_list.sort()
total = sum(n_list)
#무조건 가장 작은 숫자* 나머지 덧셈
#연산이 끝난(잘라진) 숫자는 삭제 후 재시행
for i in range(n):
    total = total - n_list[0]
    price += n_list[0] * total
    del n_list[0]

print(price)