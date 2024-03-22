import  sys
from heapq import heappop,heappush

input = sys.stdin.readline

n,e = map(int,input().strip().split())
# from collections import defaultdict
graph = {x:[] for x in range(200000+1)}
# print(graph)
for k in range(e):
    a,b,c = map(int,input().strip().split())
    graph[a].append([b,c])
    graph[b].append([a,c])


v1,v2 = map(int,input().strip().split())

# start 1: end N
# v1,v2의 최단거리를 구하면되지않을까?
# 그후 1부터 v1까지의 최단거리 ,v1 -v2의 최단거리 , v2->N까지의 최단거리
# 혹은 1부터 v2까지의 최단거리 , v1-v2의최단거리 , v1-> N까지의 최단거리
INF = float('inf')

def dijkstra(start):
    q = []
    distance = [INF for x in range(200000+1)]
    heappush(q,(0,start))
    
    distance[start]=0
    while q:
        dist, now = heappop(q)
        if distance[now] < dist:
            continue
        
        for node,node_dist in graph[now]:
            add_dist = dist + node_dist
            if add_dist < distance[node]:
                distance[node] = add_dist
                heappush(q,(add_dist,node))
    return distance


first = dijkstra(1)
mid = dijkstra(v1)
end = dijkstra(v2)


ans = min(first[v1] + mid[v2] + end[n] ,first[v2] + end[v1] + mid[n])
# print(INF)
if ans==INF:
    print(-1)
    exit()
else:
    print(ans)