from collections import deque
def solution(x, y, n):
    answer = 0
    dp=[9999 for x in range(y+1)]
    dp[x]=0
    for i in range(y):
        if dp[i]==-1:
            continue
        if i*3<=y:
            dp[i*3] = min(dp[i]+1,dp[i*3])
        if i*2 <=y:
            dp[i*2] = min(dp[i]+1,dp[i*2])
        if i+n<=y:
            dp[i+n] = min(dp[i]+1,dp[i+n])
    if dp[y]==9999:
        return -1
    return dp[y]