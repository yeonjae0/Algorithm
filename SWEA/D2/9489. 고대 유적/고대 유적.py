def count(arr):  # 가장 긴 건축물 길이 반환 함수
    mx = 2  # 건축물 길이가 최소 2라고 나와있음

    for i in arr: # i는 arr(2차원 리스트) 안의 리스트
        cnt = 0
        for j in i:
            if j == 1:
                cnt += 1
                if cnt > mx:
                    mx = cnt
            else:
                cnt = 0
    return mx



T = int(input())
for t in range(1, T+1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    arr_t = list(map(list, zip(*arr)))

    aa = count(arr)
    bb = count(arr_t)
    print(f'#{t} {max(aa, bb)}')