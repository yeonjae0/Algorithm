arr = [list(map(int, input().split())) for _ in range(9)]
max_num = 0
posi = (1, 1)
for i in range(9):
    for j in range(9):
        if arr[i][j] > max_num:
            max_num = arr[i][j]
            posi = (i+1, j+1)

print(max_num)
print(posi[0], posi[1])
