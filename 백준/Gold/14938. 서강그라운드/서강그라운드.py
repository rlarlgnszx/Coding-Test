import sys
input = sys.stdin.readline

place, m , r = map(int,input().split())
item = list(map(int,input().split()))

board=[[int(1e9) for object in range(place)] for i in range(place)]
for i in range(place):
    board[i][i]=0
for i in range(r):
    x,y,dist = map(int,input().split())
    board[x-1][y-1]= dist
    board[y-1][x-1]= dist

for k in range(place):
    for i in range(place):
        for j in range(place):
            if board[i][j] > board[i][k] + board[k][j]:
                board[i][j] = board[i][k] + board[k][j]
max_sum = 0
for i in range(place):
    temp = 0
    for j in range(place):
        if board[i][j] <= m:
            temp+= item[j]
    max_sum = max(max_sum,temp)
print(max_sum)