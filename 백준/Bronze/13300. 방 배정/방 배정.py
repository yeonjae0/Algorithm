n, k = map(int, input().split())
room = [0] * 13

for _ in range(n):
    s, g = map(int, input().split())
    ans = 0
    if s == 0:
        room[2*g-1] += 1
    else:
        room[2*g] += 1

for i in range(13):
    if room[i] != 0 and (room[i] % k == 0):
        ans += room[i] // k
    elif room[i] != 0 and (room[i] % k != 0):
        ans += room[i] // k + 1
        
print(ans)