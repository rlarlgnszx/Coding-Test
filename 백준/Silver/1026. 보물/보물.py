from heapq import heappush,heappop
def solution():
    n = int(input())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    A.sort()
    temp = []
    for j in range(n):
        heappush(temp,[-B[j],j])
    result = 0
    i = 0
    while temp:
       result -= heappop(temp)[0]*A[i]
       i+=1
    print(result)
solution()