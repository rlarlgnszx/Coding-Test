def solution(board, h, w):
    answer = 0
    check = board[h][w]
    goto = [[1,0],[0,-1],[-1,0],[0,1]]
    stack = [[h,w,check]]
    while stack:
        x,y,c = stack.pop(0)
        for a,b in goto:
            if 0<=a+x<len(board) and 0<=b+y<len(board) and board[a+x][b+y]==c:
                answer+=1
    return answer