
def recursive(i , cnt):  # i: 바꿀 시작 인덱스, cnt: 현재까지 바꾼 횟수
    global ans
    if cnt == a:
        tmp = int(''.join(list(map(str, num))))
        if tmp >= ans:
            ans = tmp
            return
    # 인덱스 맨 끝값 -> 정렬 끝남
    if i == length - 1:
        if flag:
            tmp = int(''.join(list(map(str, num))))
            if tmp >= ans:
                ans = tmp
                return
        elif (a - cnt) % 2 == 0:  # 중복 값이 없고 짝수
            tmp = int(''.join(list(map(str, num))))
            if tmp >= ans:
                ans = tmp
                return
        else:  # 중복 값이 없고, 홀수 -> 끝에 두 자리 바꿔준다
            num[-2], num[-1] = num[-1], num[-2]
            tmp = int(''.join(list(map(str, num))))
            if tmp >= ans:
                ans = tmp
                return
    max_v = max(num[i:])
    if num[i] == max_v:  # 지금 참조하는 인덱스 값이 최대
        recursive(i+1, cnt)
    else:  # 지금 참조하는 인덱스 값이 최대가 아님
        for j in range(i+1, length):
            if num[j] == max_v:
                num[i], num[j] = num[j], num[i]
                recursive(i + 1, cnt + 1)
                num[i], num[j] = num[j], num[i]

## !! 오류났던 부분 !!
# if tmp >= ans: // 이 부분에서 > 표시만 해줄 경우 같은 경우에서 return을 받지 못해 오류

T = int(input())
for tc in range(1, T+1):
    num1, a = map(str, input().split())  # a: 반복해야하는 횟수
    a = int(a)
    num = list(map(int, num1.lstrip()))
    length = len(num)
    ans = 0  # 상금 최댓값을 담아줄 변수
    flag = 0  # num 리스트 내 중복값이 없으면 0, 있으면 1
    # 리스트는 메모리에 저장되는 방식이 주소에 있는 값을 직접 참조해서 값을 바꿔주기 때문에 주소가 바뀌지 않는 이상 값이 계속 유지
    if len(num) != len(set(num)):
        flag = 1
    recursive(0, 0)
    print(f'#{tc} {ans}')
