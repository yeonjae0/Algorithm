for _ in range(10):
    t = int(input())
    ladder = [] #사다리 전체를 2차원 리스트로 받기
    clone = []
    end = 0 #도착 지점의 인덱스 값 넣기 ladder[99][end]
    for _ in range(100):
        ladder.append(list(map(int, input().split())))
        #clone.append([[0]*100])


    #end값을 찾기 위한 반복문
    for a in range(100):
        if ladder[99][a] == 2:
            end = a
    clone.append((99, end))
    #i를 한 번씩 -1
    i = 99 #위로 위로
    while i >= 0:

        if (0 <= end-1 < 100) and (ladder[i][end-1]) and ((i, end-1) not in clone):#좌
            end = end - 1
            clone.append((i, end))
        elif (0 <= end+1 < 100) and (ladder[i][end+1]) and ((i, end+1) not in clone): #우
            end = end + 1
            clone.append((i, end))

        else:

            i -= 1
            clone.append((i, end))

    print(f'#{t} {end}')