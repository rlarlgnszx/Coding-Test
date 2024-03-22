import sys
input = sys.stdin.readline
n = int(input())
from collections import defaultdict

graph = defaultdict(list)
for j in range(n-1):
    a,b,c = map(int,input().split())
    graph[a].append([b,c])
    graph[b].append([a,c])



def dfs(start):
    stack = [[start,0]]
    max_node = None
    max_dist = 0
    visited = set()
    # visited.add(start)
    while stack:
        node,dist = stack.pop()
        if dist > max_dist:
                max_node = node
                max_dist = dist
        visited.add(node)
        for next_node,next_dist in graph[node]:
            if next_node not in visited:
                visited.add(next_node)
                stack.append([next_node,next_dist+dist])
    return max_node, max_dist


start, _ = dfs(1)
# print(start,_)
_, ans = dfs(start)
# print(_,ans)
print(ans)