import sys
from collections import deque

input = sys.stdin.readline
#상자 가로, 세로, h 높이
m,n,h = map(int,input().split())

# 1 익은것, 0 안익은것, -1 없는것
one_toma = set()
no_way = set()
zero_toma = set()

# z,x,y로 표현
for a in range(h): # z
    for b in range(n): # y 
        temp = list(map(int,input().split())) # x
        for c,val in enumerate(temp):
            if val==1:
                one_toma.add((a,b,c))
            elif val==0:
                zero_toma.add((a,b,c))
            else:
                no_way.add((a,b,c))

# 다익은상태
if not zero_toma:
    print(0)
    exit()
goto = [[1,0,0],[-1,0,0],[0,1,0],[0,-1,0],[0,0,1],[0,0,-1]]
stack = one_toma.copy()
new_stack = set()
visited=  set()
count = 0
while stack:
    z,y,x = stack.pop()
    for a,b,c in goto:
        if 0<= a+z < h and 0<= y+b < n and 0<=x+c < m and (a+z,b+y,x+c) not in visited:
            visited.add((a+z,y+b,x+c))
            if (a+z,y+b,x+c) in zero_toma:
                new_stack.add((a+z,y+b,x+c))
                zero_toma.remove((a+z,y+b,x+c))
    if not stack:
        if not new_stack:
            break
        stack = new_stack.copy()
        new_stack.clear()
        count +=1
if zero_toma:
    print(-1)
else:
    print(count)
            
             