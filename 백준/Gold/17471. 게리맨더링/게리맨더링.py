# 17471 백준 게리맨더링

from collections import deque
from itertools import combinations

# 해당 그래프의 노드가 인접해있는지 체크
def bfs(lst):  # lst: 검사할 리스트
    visited = [False] * (N + 1)
    visited[0] = True
    # !!! q = deque([lst[0]]) deque 안 괄호 주의
    # 대안: queue.append(lst[0])
    q = deque([lst[0]])
    visited[lst[0]] = True

    # lst에 포함안된곳 미리 True 표시
    for y in node_lst:
        if y not in lst:
            visited[y] = True

    while q:
        node = q.popleft()
        for j in adjacent_graph[node]:
            if not visited[j]:
                q.append(j)
                visited[j] = True

# visited 전체가 True일 경우에 return True
    for l in range(1, N+1):
        if not visited[l]:
            return False
    # print(visited, lst)
    return True


def total_population(lst):
    tmp = 0
    for k in lst:
        tmp += population[k]
    # print(lst, tmp)
    return tmp


N = int(input())  # 구역의 수
population = list(map(int, input().split()))  # 구역 별 인구수
population.insert(0, 0)  # 인덱스와 노드번호 맞춰주기 1
# print(population)

adjacent_graph = [list(map(int, input().split())) for _ in range(N)]
for x in adjacent_graph:  # 맨 앞 숫자는 인접 노드의 수. 해당 숫자 제외
    x.pop(0)
adjacent_graph.insert(0, [0])  # 인덱스와 노드번호 맞춰주기 2
# print(adjacent_graph)
min_val = 1000  # 최적화하며 정답 도출할 변수
node_lst = [i for i in range(1, N+1)]  # 노드 번호 모음

for n in range(1, N//2+1):
    for combi in combinations(node_lst, n):
        n_combi = []
# combi에 들어있지 않은 숫자
        for x in node_lst:
            if x not in combi:
                n_combi.append(x)
        # print('combi', combi)
        # print('n_combi', n_combi)

        if bfs(combi) and bfs(n_combi):
            #     print('c', total_population(combi), combi)
            #     print('nc', total_population(n_combi), n_combi)
            #     print('abs', abs(total_population(combi)) - total_population(n_combi))
            min_val = min(min_val, abs((total_population(combi)) - total_population(n_combi)))



if min_val == 1000:
    print(-1)
else:
    print(min_val)