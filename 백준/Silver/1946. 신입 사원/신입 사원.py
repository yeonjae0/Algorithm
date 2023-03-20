tc = int(input())
for _ in range(tc):
    lst = []
    n = int(input())
    for _ in range(n):
        resume, interview = map(int, input().split())
        lst.append([resume, interview])
    lst.sort()
    # 서류 1등은 무조건 통과 그 뒤의 사원들은 서류 1위보다 면접랭크 높아야 함. standard보다
    # 면접 랭크가 높으면 통과시키고 standard도 업뎃하자
    standard = lst[0][1]
    cnt = 1
    for i in range(1, n):
        if lst[i][1] < standard:
            cnt += 1
            standard = lst[i][1]
    # print(lst)
    print(cnt)