# 1138 백준 한 줄로 서기

N = int(input())
lst = list(map(int, input().split()))
ans = [0] * N

for i in range(1, N+1):
    cnt = 0  # 왼쪽에서 키 큰 사람 카운트
    # if i == 1:
    #     ans[lst[i-1]+1] = 1
    for j in range(N):
        if cnt == lst[i-1] and ans[j] == 0:     # 키 큰 사람의 수가 리스트 숫자와 같을 떄
            ans[j] = i
            break
        elif ans[j] == 0:  # 빈 자리가 곧 키 큰 사람 / 채워져 있으면 넘어가야함
            cnt += 1
print(*ans)



