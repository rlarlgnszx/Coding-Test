import sys
import heapq

input = sys.stdin.readline

n, k = map(int, input().split())
gems = [list(map(int, input().split())) for _ in range(n)]
bags = [int(input().strip()) for _ in range(k)]

# 정답
gems.sort()
bags.sort()

result = 0
heap = []
for bag in bags:
    while gems and gems[0][0] <= bag:
        heapq.heappush(heap, -gems[0][1])
        heapq.heappop(gems)
    if heap:
        result -= heapq.heappop(heap)
print(result)