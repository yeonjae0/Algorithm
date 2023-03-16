from heapq import heappush, heappop

n = int(input())
heap = []
for _ in range(n):
    lst = map(int, input().split())
    for i in lst:
        if len(heap) < n:
            heappush(heap, i)
        else:
            if i > heap[0]:
                heappop(heap)
                heappush(heap, i)
print(heappop(heap))