n = int(input())
n_list = list(map(int, input().split()))
ans = []

for j in range(1, n+1): 
    a = j-1-n_list[j-1]
    # if a < 0:
    #     a = 0
    ans.insert(a, j)

for i in ans:
    print(i, end = ' ')