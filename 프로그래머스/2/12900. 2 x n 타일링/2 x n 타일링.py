def solution(n):
    answer = 0
    dp = [0 for x in range(n+1)]
    dp[1]=1
    if n==1 or n==2:
        return n
    dp[2]=2
    for i in range(3,n+1):
        dp[i] = (dp[i-2]+ dp[i-1])%1_000_000_007
        
    return dp[n]