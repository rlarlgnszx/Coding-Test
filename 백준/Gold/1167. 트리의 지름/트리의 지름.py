import sys
from collections import deque , defaultdict
from heapq import heappop,heappush
n = int(input())
graph = defaultdict(list)
for i in range(n):
    temp = deque(map(int,sys.stdin.readline().strip().split()))
    x = temp.popleft()
    while temp:
        y = temp.popleft()
        if y==-1:
            break
        d = temp.popleft()
        graph[x].append([y,d])

# print(graphW)
# while 
# graph x => [y, y와의 거리]
max_d = 0

stack = deque(x for x in graph[1])
# find far from 1
visited = defaultdict(int)
# print(graph[1])
visited[1]=0
for f in graph[1]:
    visited[f[0]]=f[1]

while stack:
    y,d = stack.popleft()
    for j in graph[y]:
        if j[0] not in visited:
            stack.append([j[0],d+j[1]])
            visited[j[0]]=d+j[1]
        elif visited[j[0]] > d+j[1]:
            visited[j[0]]=d+j[1]
            # stack.append([j[0],d+j[1]])
        
# print(visited)
# print(max(visited.values()))
find_first_root = 0
find_max = 0
for k in visited:
    if visited[k] > find_max:
        find_first_root = k
        find_max = visited[k]

# print(find_first_root)
stack = deque(x for x in graph[find_first_root])
# find far from 1
visited = defaultdict(int)
# print(graph[1])
visited[find_first_root]=0

for f in graph[find_first_root]:
    visited[f[0]]=f[1]

while stack:
    y,d = stack.popleft()
    for j in graph[y]:
        if j[0] not in visited:
            stack.append([j[0],d+j[1]])
            visited[j[0]] = d+j[1]
        elif visited[j[0]] > d+j[1]:
            visited[j[0]]= d+j[1]
            # stack.append([j[0],d+j[1]])

# print(visited)
print(max(visited.values()))