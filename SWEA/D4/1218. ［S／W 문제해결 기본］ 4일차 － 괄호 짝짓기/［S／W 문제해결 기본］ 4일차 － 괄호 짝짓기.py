
for t in range(1, 11):
    n = int(input())
    str = list(input())  # 문자열 넣어주기
    lst = ['(', ')', '{', '}','[',']','<','>']

    stack = []
    top = -1
    for i in str:
        if (len(stack) == 0) and (i in lst):
            stack.append(i)

        elif (len(stack) != 0) and (stack[top] == '(') and (i == ')'):
            stack.pop()

        elif (len(stack) != 0) and (stack[top] == '{') and (i == '}'):
            stack.pop()
            
        elif (len(stack) != 0) and (stack[top] == '[') and (i == ']'):
            stack.pop()
            
        elif (len(stack) != 0) and (stack[top] == '<') and (i == '>'):
            stack.pop()

        elif i in lst:
            stack.append(i)

    if len(stack) == 0:
        print(f'#{t} 1')
    else:
        print(f'#{t} 0')