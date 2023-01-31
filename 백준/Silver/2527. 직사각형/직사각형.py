for i in range(4):   
    x1, y1, p1, q1, x2, y2, p2, q2 = map(int,input().split())


    #점 4개
    if ((x1, y1) == (p2, q2)) or ((p1, y1) == (x2, q2)) or ((x1, q1) == (p2, y2)) or ((p1, q1) == (x2, y2)):
        print('c')

    #위 아래로 접할 때
    elif (((y1 == q2) or (q1 == y2)) and (len(set(range(x1, p1+1)) & set(range(x2, p2+1))) != 0)):
        print('b') 

    #양 옆 세로로 접할 때
    elif (((x1 == p2) or (p1 == x2)) and (len(set(range(y1, q1+1)) & set(range(y2, q2+1))) != 0)): 
        print('b')

    #겹칠 때 and를 기점으로 왼쪽이 
    elif (len(set(range(x1, p1+1)) & set(range(x2, p2+1)))) and (len(set(range(y1, q1+1)) & set(range(y2, q2+1)))):
        print('a')
    else:
        print('d')