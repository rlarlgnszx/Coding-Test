import sys
input =sys.stdin.readline
from heapq import heappop,heappush
from collections import defaultdict
city = int(input())
bus = int(input())
graph = defaultdict(list)
for i in range(bus):
    x,y,cost = map(int,input().split())
    graph[x].append((cost,y))

start,end = map(int,input().split())

def djk(start,end):
    q = []
    distance = [int(1e9) for x in range(city+1)]
    distance[start] = 0
    heappush(q,(0,start))
    while q:
        dist,cur = heappop(q)
        if distance[cur] < dist:
            continue
        for next_dist,next_cur in graph[cur]:
            cost = next_dist + dist
            if cost < distance[next_cur]:
                distance[next_cur] = cost
                heappush(q,(cost,next_cur))
    return distance[end]

print(djk(start,end))