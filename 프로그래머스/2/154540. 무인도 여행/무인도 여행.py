from collections import deque
def solution(maps):
    answer = []
    goto = [[1,0],[0,1],[-1,0],[0,-1]]
    r = len(maps)
    c = len(maps[0])
    maps = [[t for t in x] for x in maps]
    def start(x,y):
        ans = 0
        stack = deque([[x,y]])
        ans += int(maps[x][y])
        maps[x][y] = 'X'
        while stack:
            cur_x,cur_y = stack.popleft()
            for a,b in goto:
                nx,ny = a+cur_x,b+cur_y
                if 0<=nx<r and 0<=ny<c and maps[nx][ny]!='X':
                    stack.append([nx,ny])
                    ans+= int(maps[nx][ny])
                    maps[nx][ny]='X'
        answer.append(ans)
    for i in range(r):
        for j in range(c):
            if maps[i][j]!='X':
                start(i,j)
                
    answer.sort()
    if len(answer)>0:
        return answer
    return [-1]


