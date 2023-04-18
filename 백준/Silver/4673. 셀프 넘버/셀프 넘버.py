def solution():
    dp=[False for x in range(10000+1)]
    def sansung(n):
        n += sum(map(int,list(str(n))))
        try:
            dp[n]=True
        except:
            pass
    for i in range(10000):
        sansung(i)
    for j in range(10000):
        if not dp[j]:
            print(j)
solution()