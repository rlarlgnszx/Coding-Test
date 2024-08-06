import sys
input =sys.stdin.readline
from heapq import heappop,heappush

class DisjoinSet:
    def __init__(self,n):
        self.parent = list(range(n+1))
        self.rank = [0]*(n+1)
    def find(self,x):
        if self.parent[x] != x:
            self.parent[x] =  self.find(self.parent[x])
        return self.parent[x]
    def union(self,x,y):
        rootX= self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootY] > self.rank[rootX]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1


def kruskal(V,edges):
    edges.sort(key=lambda x: x[2])
    mst = []
    ds = DisjoinSet(V)
    mst_weight = 0
    for u,v,cost in edges:
        if ds.find(u) != ds.find(v):
            ds.union(u,v)
            mst.append(cost)
            mst_weight += cost

    return mst_weight

V, E = map(int, input().split())
edges = []

for _ in range(E):
    A, B, C = map(int, input().split())
    edges.append((A, B, C))

# 최소 스패닝 트리의 가중치 계산
result = kruskal(V, edges)
print(result)