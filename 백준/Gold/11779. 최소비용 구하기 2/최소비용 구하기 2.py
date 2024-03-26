import sys
input= sys.stdin.readline

n = int(input())
m = int(input())
from collections import defaultdict
graph = defaultdict(list)
for j in range(m):
    x,y,d = map(int,input().split())
    graph[x].append([y,d])
start,end = map(int,input().split())

from heapq import heappop,heappush
def dijsktra(start,end):
    q = []
    distance = [int(1e9) for x in range(n+1)]
    distance[start]=0
    heappush(q,(0,start,[start]))
    answer_city_len = int(1e9)
    answer_city = []
    while q:
        dist,start,citys = heappop(q)
        if dist > distance[start]:
            continue
        for node,next_dist in graph[start]:
            cost = next_dist+ dist
            if cost < distance[node]:
                distance[node] = cost
                k = citys.copy()
                k.append(node)
                heappush(q,(cost,node,k))
                if node ==end:
                    answer_city = k
                    answer_city_len = len(k)
    
    return distance[end],answer_city_len,answer_city

ans,ans2,ans3 = dijsktra(start,end)
print(ans)
print(ans2)
print(" ".join(map(str,ans3)))