N = int(input())
x_list = []
y_list = []
lst = [list(map(int, input().split())) for _ in range(N)]
for posi in lst:
  x_list.append(posi[0])
  y_list.append(posi[1])

if N <= 1:
    print(0)
elif len(set(x_list)) <= 1 or len(set(y_list)) <= 1:
   print(0)
else:
   ans  = (max(x_list)-min(x_list)) * (max(y_list)- min(y_list))
   print(ans)