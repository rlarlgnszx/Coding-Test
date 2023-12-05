from collections import deque
# from typing import Deque
import time
class Board:
    def __init__(self,board,k) -> None:
        self.k=k
        self.board=board# for left,right
        self.board2 = deque(map(deque,(zip(*board)))) # for top,down
        self.max = 0
        for j in self.board:
            for f in j:
                self.max = max(f,self.max)
        
    def goto(self,list,show=False):
        for n in list:
            # 
            if n==0:
                self.go_down()
                if show:
                    print('Down')
            elif n==1:
                self.go_left()
                if show:
                    print('Left')
            elif n==2:
                self.go_right()
                if show:
                    print('Right')
            else:
                self.go_top()
                if show:
                    print("Top")
            if show:
                print(f'==============={n}================')
                self.show()
        return self.max

    def go_top(self):
        new_list = deque()
        for c in self.board2:
            do_it = False
            rest_list = deque([])
            new_col =deque([])
            new_c = c.copy()
            for num in new_c:
                if num==0:
                    rest_list.append(0)
                    # do_it=False
                elif new_col:
                    if new_col[-1]==num and do_it==False:
                        new_col[-1]=num*2
                        self.max = max(new_col[-1],self.max)
                        do_it=True
                    elif num:
                        new_col.append(num)
                        do_it=False
                else:
                    new_col.append(num)
                    do_it=False
            new_col += rest_list
            while len(new_col)<self.k:
                new_col.append(0)
            new_list.append(new_col)
            do_it = False
        
        self.board2 = new_list
        self.board = deque(map(deque,(zip(*self.board2))))
    def go_left(self):
        new_list = deque([])
        do_it = False
        for c in self.board:
            do_it = False
            rest_list = deque([])
            new_col =deque([])
            new_c = c.copy()
            for num in new_c:
                if num==0:
                    rest_list.append(0)
                    # do_it=False
                elif new_col:
                    if new_col[-1]==num and do_it==False:
                        new_col[-1]=num*2
                        self.max = max(new_col[-1],self.max)
                        do_it=True
                    elif num!=0:
                        new_col.append(num)
                        do_it=False
                else:
                    new_col.append(num)
                    do_it=False
            new_col += rest_list
            while len(new_col)<self.k:
                new_col.append(0)
            new_list.append(new_col)
            do_it = False
        # pass
        self.board = new_list
        self.board2 = deque(map(deque,(zip(*self.board))))
    def go_right(self):
        new_list = deque([])
        do_it = False
        for c in self.board:
            do_it = False
            rest_list = deque([])
            new_col =deque([])
            new_c = c.copy()
            new_c.reverse()
            while new_c:
                num = new_c.popleft()
                if num==0:
                    rest_list.appendleft(0)
                    # do_it=False
                elif new_col:
                    if new_col[0]==num and do_it==False:
                        new_col[0]=num*2
                        self.max = max(new_col[0],self.max)
                        do_it=True
                    elif num!=0:
                        new_col.appendleft(num)
                        do_it=False
                else:
                    new_col.appendleft(num)
                    do_it=False
            rest_list+= new_col
            while len(rest_list)<self.k:
                rest_list.appendleft(0)
            new_list.append(rest_list)
            do_it = False
        # pass
        self.board = new_list
        self.board2 = deque(map(deque,(zip(*self.board))))
    def go_down(self):
        new_list = deque([])
        for c in self.board2:
            do_it = False
            rest_list = deque([])
            new_col =deque([])
            new_c = c.copy()
            new_c.reverse()
            while new_c:
                num = new_c.popleft()
                if num==0:
                    rest_list.appendleft(0)
                    # do_it=False
                elif new_col:
                    if new_col[0]==num and do_it==False:
                        new_col[0]=num*2
                        self.max = max(new_col[0],self.max)
                        do_it=True
                    elif num:
                        new_col.appendleft(num)
                        do_it=False
                else:
                    new_col.appendleft(num)
                    do_it=False
            rest_list+= new_col
            while len(rest_list)<self.k:
                rest_list.appendleft(0)
            new_list.append(rest_list)
            do_it = False
        # pas
        self.board2 = new_list
        # print(self.board2)
        self.board = deque(map(deque,(zip(*self.board2))))

    def show(self):
        for k in self.board:
            for j in k:
                print ( j,end= ' ')
            print()

    def get_max(self):
        return self.max
import sys
k = int(sys.stdin.readline().strip())
board = [deque(map(int,sys.stdin.readline().strip().split())) for x in range(k)]

from itertools import product
j = [x for x in range(4)]
per = list(product(j,repeat=5))
mt = 0
test_p = None
for p in per:
    board_int = board.copy()
    temp = Board(board_int,k)
    new_temp = temp.goto(p)
    if new_temp> mt:
        test_p = p
        tmp = Board(board,k)
        tmp.goto(p)
    mt = max(new_temp,mt)

# print(test_p)
# a = Board(board,k)
# t = [0]
# a.goto(test_p,True)
print(mt)
# # a.goto([3],True)
# for i in range(4):
#     a = Board(board,k)
#     a.goto([i],True)
