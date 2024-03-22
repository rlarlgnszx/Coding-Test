from heapq import heappop,heappush
import sys
input = sys.stdin.readline

v,e = map(int,input().split())
start = int(input())
from collections import defaultdict

graph = defaultdict(list)

for i in range(e):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))


INF = int(1e9)
def djikstra(start):
    q = []
    distance =  [INF for x in range(20_000+1)]
    heappush(q,(0,start))
    distance[start]= 0    
    while q:
        dist, cur = heappop(q)
        if distance[cur] < dist:
            continue
        
        for next_node ,next_dist in graph[cur]:
            next_cost = dist + next_dist
            if next_cost < distance[next_node]:
                distance[next_node] = next_cost
                heappush(q,(next_cost,next_node))
    return distance

distance = djikstra(start)

for i in range(1,v+1):
    temp = distance[i]
    if temp == INF:
        print('INF')
    else:
        print(temp)
    
