# 백준 1446 지름길  (다익스트라, dp)

import heapq
# import sys
# sys.stdin = open("input.txt", "r", encoding='UTF-8')

INF = int(1e9)
# n: 지름길의 개수 / d: 고속도로의 길이
n, d = map(int, input().split())
graph = [[]for _ in range(d+1)]  # 거리 하나하나를 노드로
# 지름길의 정보를 저장한다
# 그래프의 인데스 번호
distance = [INF] * (d+1)

# 다익스트라 함수만들기
def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정. 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:  # q가 빌 때까지
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들 확인
        for i in graph[now]:
            cost = dist + i[1]  # i[1]은 i[0]으로 가는 비용
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

# j번에서 j+1로 가는 거리는 무조건 1
# j번에서 (도착지점, 도착지점으로 가기 위해 가야하는 거리)
for j in range(d):
    graph[j].append((j+1, 1))

# 지름길을 입력받아서 업데이트
for _ in range(n):
    s, e, shortcut = map(int, input().split())
    if d < e:  # 필요없는 지름길 (가야하는 지점보다 멀리감)
        continue
    graph[s].append((e, shortcut))
dijkstra(0)
print(distance[d])
