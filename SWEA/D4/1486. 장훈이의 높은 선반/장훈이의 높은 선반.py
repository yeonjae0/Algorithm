# SWEA 1486 장훈이의 높은 선반

def dfs(i, sm):  # height의 인덱스 / 합
    global ans

# 가지치기
    if ans <= sm - B:
        return

# 종료조건(필수!!)
    if i == n:
        if sm >= B:
            ans = min(ans, sm-B)
        return


    dfs(i+1, sm + height[i])
    dfs(i+1, sm)



T = int(input())
for tc in range(1, T+1):
    n, B = map(int, input().split())
    height = list(map(int, input().split()))
    ans = 100000 * 20
    dfs(0, 0)
    print(f'#{tc} {ans}')