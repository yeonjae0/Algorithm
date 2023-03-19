from collections import deque

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())  # n은 문서 개수, m은 현재 몇 번쨰
    lst = list(map(int, input().split()))
    q = deque([])
    for i, num in enumerate(lst):
        q.append((num, i))
    cnt = 1

    while True:
        if q and q[0][0] == max(q)[0]:
            a = q.popleft()

            if a[1] == m:
                break
            cnt += 1
        else:
            q.append(q.popleft())
    print(cnt)