
# 계단 규칙
# 한번에 한계단 or 2계단
# 이전에 두계단 두계단이면 또 두계단 불가능
## 마지막 도착 계단은 무조건 밟아야한대


import sys
input = sys.stdin.readline

n = int(input())
dp= [0] * (n+1)
# dp -> 밟은 계단의 연속된 수,값
stairs =[0]+[int(input()) for x in range(n)]
if n==1:
    print(stairs[1])
    exit()
elif n==2:
    print(sum(stairs))
    exit()
dp[1] = stairs[1]
dp[2] = stairs[1]+stairs[2]
for k in range(3,n+1):
    dp[k] = max(dp[k-3]+(stairs[k-1]+stairs[k]), dp[k-2]+stairs[k])

print(dp[-1])


