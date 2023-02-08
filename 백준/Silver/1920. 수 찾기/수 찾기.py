n = int(input())
n_list = list(map(int, input().split()))
n_list.sort()
m = int(input())
m_list = list(map(int, input().split())) #이 수들이 n_list 안에 존재하는지 확인

for i in m_list:
    start = 0
    end = n - 1 #인덱스값이라 -1 / 0부터 시작
    ans = 0
    while start <= end:
        cut = (start + end) // 2

        if i > n_list[cut]: #오른쪽 확인
            start = cut + 1

        elif i < n_list[cut]: #왼쪽 확인
            end = cut -1

        else:
            ans = 1
            break
    print(ans)