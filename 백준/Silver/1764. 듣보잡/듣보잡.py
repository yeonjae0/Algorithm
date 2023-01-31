N, M = list(map(int, input().split(' ')))
li= set()
se = set()
result = []

for i in range(N): #N만큼의 인풋을 li set에
    li.add(input())

for j in range(M): #M만큼의 인풋을 se set에
    se.add(input())

for x in (li & se):
    result.append(x)
    
sorted(result)
print(len(li & se))

for y in sorted(result):
   print(y)