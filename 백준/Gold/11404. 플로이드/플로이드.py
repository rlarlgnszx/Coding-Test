import sys
input =sys.stdin.readline

n = int(input())
bus = int(input())
graph = [[float('inf') for _ in range(n)] for _ in range(n)]
for i in range(bus):
    a,b,c = map(int,input().split())
    graph[a-1][b-1] = min(graph[a-1][b-1], c)
for i in range(n):
    graph[i][i] = 0

for k in range(n):
    for i in range(n):
        for j in range(n):
            graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])
for j in graph:
    for k in j:
        if k==float("inf"):
            print(0, end = " ")
        else:
            print(k,end = " ")
    print()