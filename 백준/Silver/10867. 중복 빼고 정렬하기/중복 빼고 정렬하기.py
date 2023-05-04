from heapq import heappop,heappush,heapify
def solution():
    n = int(input())
    set2 = set(map(int,input().split()))
    temp=[]
    for j in set2:
        heappush(temp,j)
    while temp:
        print(heappop(temp),end=" ")
solution()