def in_order(n):
    if n:
        in_order(int(data[n][2]))
        # print(data[n][1], end=' ')
        lst.append(data[n][1])
        in_order(int(data[n][3]))

def post_order(n):
    if n:
        post_order(int(data[n][2]))
        post_order(int(data[n][3]))
        # print(data[n][1], end=' ')
        lst.append(data[n][1])
    return lst

for t in range(1, 11):
    n = int(input())
    data = [input().split() for _ in range(n)]
    data.insert(0,[0, 0, 0, 0])

    for i in data:
        while len(i) != 4:
            i.append('0')
    lst = []
    # print(data)
    post_order(1)
    # print(lst)
    # in_order(1)

    # lst에 저장된 애들을 후위표기법으로 계산하기
    stack = []
    for j in lst:
        if j == '+':
            stack.append(stack.pop() + stack.pop())
        elif j == '-':
            k = stack.pop()
            stack.append(stack.pop() - k)
        elif j == '*':
            stack.append(stack.pop() * stack.pop())
        elif j == '/':
            k = stack.pop()
            stack.append(stack.pop() // k)
        else:
            stack.append(int(j))
    print(f'#{t}', end=' ')
    print(*stack)
