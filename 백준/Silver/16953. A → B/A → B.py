import sys
input = sys.stdin.readline
from collections import deque
def def1(a):
    return a*2
def def2(a):
    return a*10+1

a,b = map(int,input().strip().split())
stack = deque([[a,1]])

while stack:
    num, count = stack.popleft()
    fisrt = def1(num)
    second = def2(num)
    if fisrt == b or second == b:
        print(count+1)
        exit(0)
        break
    if fisrt <b:
        stack.append([fisrt,count+1])
    if second <b:
        stack.append([second,count+1])
print(-1)