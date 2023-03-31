# SWEA 2871 부분 수열의 합
# 백트래킹 -> 가능한 모든 경우를 실행해서 답을 도출

def dfs(i, sm):  # i:num의 인덱스 / sm: 수열의 합
    global cnt

    # [3]가지치기: 더 이상 접답 갱신 가능성 없는 경우
    # 가장 마지막에, 가장 위쪽에
    if sm > k:
        return

    # [1] 종료조건(n에 관련): 반드시 정답처리는 이곳에서만!!!
    if i == n:  # n-1까지는 돌아야함
        if sm == k:
            cnt += 1
        return

    # [2] 하부호출
    dfs(i+1, sm + num[i])  # 해당 숫자가 포함되는 경우
    dfs(i+1, sm)           # 해당 숫자가 포함되지 않는 경우




T = int(input())
for tc in range(1, T+1):
    n, k = map(int, input().split())  # n: 수열의 길이 k: 구할 부분수열의 합계
    num = list(map(int, input().split()))
    cnt = 0  # 정답. 부분수열의 합이 k가 되는 개수'
    dfs(0, 0)
    print(f'#{tc} {cnt}')
