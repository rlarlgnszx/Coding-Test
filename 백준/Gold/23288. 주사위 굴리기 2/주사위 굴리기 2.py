# 주사위 굴러가는 함수
from collections import deque
class Dice:
    def __init__(self) -> None:
        self.top = deque([2,1,5,6])
        self.down = deque([4,1,3])
        self.current_index=  1

    def go_left(self):
        
        self.down.append(self.top.pop())
        self.top.append(self.down.popleft())
        self.top[self.current_index] = self.down[self.current_index]
        
    def go_right(self):
        self.down.appendleft(self.top.pop())
        self.top.append(self.down.pop())
        self.top[self.current_index] = self.down[self.current_index]
    
    
    def go_top(self):
        self.top.append(self.top.popleft())
        self.down[self.current_index]= self.top[self.current_index]
        
    def go_down(self):
        self.top.appendleft(self.top.pop())
        self.down[self.current_index]= self.top[self.current_index]
    
    
    def show(self):
        # print(self.top,self.down)
        print(' =============================')
        for i in range(4):
            for j in range(3):
                if j==1:
                    print(self.top[i],end=" ")
                else:
                    if i==1:
                        print(self.down[j],end=' ')
                    else:
                        print(' ',end=' ')
            print('\n')
            
    def get_down(self):
        return self.top[3]

import sys
import time
n,m ,k = map(int,sys.stdin.readline().split(' '))
board = [list(map(int,sys.stdin.readline().split(' '))) for x in range(n)]
# print('동쪽')
def go_ESWN(cur_x,cur_y,value):
    goto = [[0,1],[0,-1],[1,0],[-1,0]]
    stack = [[cur_x,cur_y]]
    count = 0
    score = value
    visited = set()
    visited.add((cur_x,cur_y))
    # print('XY -> ', cur_x,cur_y ,end =" " )
    while stack:
        x,y = stack.pop(0)
        # print(x,y ," :-> ",end='')
        
        count +=1
        for [a,b] in goto:
            if 0<= (a+x) < n and 0<=(b+y) < m  and board[a+x][b+y]==value:
                if (a+x,y+b) not in visited:
                    stack.append([a+x,b+y])
                    visited.add((a+x,y+b))
    
    # print('get ', count*score)
    # print(' \n')
    return count* score

x,y = [0,1]
ans = 0
goto2 = [[0,1],[1,0],[0,-1],[-1,0]]
dice = Dice()
dice.go_right()
cur_i = 0
# print(dice.show())
val = board[x][y]
cur_go = goto2[cur_i]
temp = go_ESWN(x,y,val)
ans+=temp
if dice.get_down() > val:
    try:
        cur_i+=1
        cur_go = goto2[cur_i]
    except:
        cur_i=0
        cur_go = goto2[cur_i]
elif dice.get_down()<val:
    cur_i-=1
    if cur_i<0:
        cur_i = 3
    cur_go = goto2[cur_i]

if not(0<=x+cur_go[0]<n and 0<=y+cur_go[1]<m):
    if cur_i<2:
        cur_i +=2
    else:
        cur_i -=2
    cur_go = goto2[cur_i] 
x,y = x+cur_go[0],y+cur_go[1]
if cur_i==0:
    dice.go_right()
    # print('동쪽')
elif cur_i==1:
    dice.go_down()
    # print('남쪽')
elif cur_i==2:
    dice.go_left()
    # print('서쪽')
else:
    dice.go_top()
    # print('북쪽')
for i in range(k-1):
    val = board[x][y]
    cur_go = goto2[cur_i]
    temp = go_ESWN(x,y,val)
    ans+=temp
    if dice.get_down() > val:
        try:
            cur_i+=1
            cur_go = goto2[cur_i]
        except:
            cur_i=0
            cur_go = goto2[cur_i]
    elif dice.get_down()<val:
        cur_i-=1
        if cur_i<0:
            cur_i = 3
        cur_go = goto2[cur_i]
    
    if not(0<=x+cur_go[0]<n and 0<=y+cur_go[1]<m):
        if cur_i<2:
            cur_i +=2
        else:
            cur_i -=2
        cur_go = goto2[cur_i] 
    x,y = x+cur_go[0],y+cur_go[1]
    if cur_i==0:
        dice.go_right()
    elif cur_i==1:
        dice.go_down()
    elif cur_i==2:
        dice.go_left()
    else:
        dice.go_top()
    # print('DICE COUNT :',i)
    # dice.show()
print(ans)
# dice.show()
# dice = Dice()
# dice.show()
# dice.go_left()
# dice.show()
# dice.go_right()
# dice.show()