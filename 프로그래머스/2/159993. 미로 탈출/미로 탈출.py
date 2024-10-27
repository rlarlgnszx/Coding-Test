from collections import deque
def solution(maps):
    answer = 0
    #S : 시작
    #E : 출구
    #L : 레버
    #O : 통로
    #X : 벽
    def bfs(x,y,maps,end):
        stack = deque([[x,y,0]])
        goto = [[1,0],[0,-1],[-1,0],[0,1]]
        visit = set()
        visit.add((x,y))
        while stack:
            nx,ny,time = stack.popleft()
            for c,d in goto:
                ni,nj = nx+c,ny+d
                if 0<=ni<len(maps) and 0<=nj<len(maps[0]) and maps[ni][nj] != 'X' and (ni,nj) not in visit:
                    if maps[ni][nj]==end:
                        return ni,nj,time+1
                    visit.add((ni,nj))
                    stack.append([ni,nj,time+1])
        return -1,-1,-1
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j]=="S":
                a,b,time1 = bfs(i,j,maps,'L')
                if a<0:
                    return -1
                a,b,time2 = bfs(a,b,maps,'E')
                if a<0:
                    return -1
                else:
                    return time1+time2