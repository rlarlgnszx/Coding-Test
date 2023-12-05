# 인구차이 - a
# L<=a<=R
# 국경선 open
# 전부 열린국경선 -> 인구이동 시작
## 나라 여러개 -> 인접한 칸  (연합의 인구수) / (연합을 이루고 있는 칸의 개수)
# 연합 해체후 닫음

import sys
from collections import deque
from itertools import product
N,L,R = map(int,sys.stdin.readline().strip().split())

world = [list(map(int,sys.stdin.readline().strip().split())) for k in range(N)]

visited = set()


def open_world_from_xy(cur,world,visited):
    stack = deque([cur]) # x,y, val
    grouph = set()
    grouph.add((cur[0],cur[1]))
    grouph_val = 0
    grouph_count = 0
    goto = [[1,0],[-1,0],[0,1],[0,-1]]
    visited = set()
    visited.add((cur[0],cur[1]))
    # print(visited)
    while stack:
        x,y,val = stack.popleft()
        grouph_val+= val
        grouph_count +=1
        for a,b in goto:
            if (0<=a+x< N) and (0<=b+y< N):
                next_val = world[a+x][b+y]
                if (L<=abs(next_val-val)<=R )and (a+x,b+y) not in visited:
                    # print(f"{[x,y]} : {val}=> {[x+a,b+y]} : {next_val}")
                    # print(a+x,b+y)
                    visited.add((a+x,b+y))
                    grouph.add((a+x,b+y))
                    stack.append([a+x,b+y,next_val])

    change_value  = int(grouph_val/grouph_count)
    # for k in grouph:
    #     # print(k)
    #     world[k[0]][k[1]] = change_value
    change_value
    return visited,change_value
day = 0
p = [x for x in range(N)]
import time
while 1:
    where_to_visited = deque(product(p,repeat=2))
    visited=set()
    # print(f"DAY :{day}")
    check = False
    after_change= []
    while where_to_visited:
        x,y  = where_to_visited.popleft()
        if (x,y) in visited:
            continue
        visited,change_val = open_world_from_xy([x,y,world[x][y]],world,visited)
        if len(visited)>1:
            check=True
            after_change.append([visited,change_val])
        # print(f'====={visited}=====')
        # for j in world:
        #     for f in j:
        #         print(f,end= ' ')
        #     print()
    # print("CHEK : ",check)
    if not check:
        break
    if after_change:
        for k in after_change:
            val = k[1]
            visited_list = k[0]
            # print("visited list" ,visited_list)
            for xy in visited_list:
                x,y = xy[0],xy[1]
                world[x][y] = val
    day +=1
print(day)