n = int(input())

d = [0] * (n+1) #연산의 최솟값 저장

for i in range(2, n+1):
    d[i] = d[i-1] + 1

    if i % 2 == 0:
        d[i] = min(d[i], d[i//2]+1)
    if i % 3 == 0:
        d[i] = min(d[i], d[i//3]+1) #2로 나누는 케이스보다 연산이 적으면 바뀜

print(d[n])