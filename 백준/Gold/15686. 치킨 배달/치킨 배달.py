import sys
from itertools import combinations
def solution():
    n,m = map(int,input().split())
    board= []
    house = []
    chick = []
    
    for j in range(n):
        temp = list(map(int,sys.stdin.readline().strip().split()))
        for i,data in enumerate(temp):
            if data==1:
                house.append([j,i])
            elif data==2:
                chick.append([j,i])
    city_chick = list(combinations(chick,m))
    result = float('inf')
    for city in city_chick:
        sum_chick = 0
        for ho in house:
            min_ho = float('inf')
            for k in city:
                min_ho = min(min_ho,abs(ho[0]-k[0])+abs(ho[1]-k[1]))
            sum_chick+=min_ho
        result = min(result,sum_chick)
    print(result)
solution()
        
        