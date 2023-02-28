lst = []
N = int(input())
for _ in range(N):
    name, kor, eng, math = map(str, input().split())
    lst.append([name, int(kor), int(eng), int(math)])
# 리스트끼리 여러 개의 원소를 가지고 있을 때 앞의 인덱스끼리 정렬하고 그 다음으로 다음 조건대로 정렬 가능
# - 는 reverse = True와 같은 기능 (내림차순)
lst.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))

for i in lst:
    print(i[0])