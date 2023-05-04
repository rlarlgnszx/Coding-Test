cnt =0
def solution():
    global cnt
    n,m = map(int,input().split())
    temp = list(map(int,input().split()))
    def dfs(data,sol,level):
        global cnt
        # print(sol)
        if sol and sum(sol)==m:
            cnt+=1
        for i in range(level,n):
            sol.append(data[i])
            dfs(data,sol,i+1)
            sol.pop()
    dfs(temp,[],0)
    print(cnt)
solution()