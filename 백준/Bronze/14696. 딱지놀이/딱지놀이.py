# 14696 백준 딱지놀이

def win(alst, blst):
    if alst.count(4) > blst.count(4):
        return print('A')
    elif alst.count(4) < blst.count(4):
        return print('B')

    elif (alst.count(4) == blst.count(4)) and alst.count(3) > blst.count(3):
        return print('A')
    elif (alst.count(4) == blst.count(4)) and alst.count(3) < blst.count(3):
        return print('B')

    elif (alst.count(4) == blst.count(4)) and (alst.count(3) == blst.count(3)) \
            and (alst.count(2) > blst.count(2)):
        return print('A')
    elif (alst.count(4) == blst.count(4)) and (alst.count(3) == blst.count(3)) \
         and (alst.count(2) < blst.count(2)):
        return print('B')

    elif (alst.count(4) == blst.count(4)) and (alst.count(3) == blst.count(3)) \
        and (alst.count(2) == blst.count(2)) and (alst.count(1) > blst.count(1)):
        return print('A')
    elif (alst.count(4) == blst.count(4)) and (alst.count(3) == blst.count(3)) \
         and (alst.count(2) == blst.count(2)) and (alst.count(1) < blst.count(1)):
        return print('A')

    else:
        return print('D')



T = int(input())
for _ in range(T):
    A = list(map(int, input().split()))
    del A[0]
    B = list(map(int, input().split()))
    del B[0]

    win(A, B)