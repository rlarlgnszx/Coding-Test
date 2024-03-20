n = int(input())
board=  list(map(int,input().split()))
max2= max(board)

board = list(map(lambda x:x/max2*100 ,board))
print(sum(board)/len(board))
