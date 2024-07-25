import sys
input = sys.stdin.readline

n, k = map(int, input().split())
bags = []

for _ in range(n):
    weight, value = map(int, input().split())
    bags.append((weight, value))

# DP 배열 초기화
dp = [0] * (k + 1)

# 각 물건을 반복하며 DP 처리
for weight, value in bags:
    for j in range(k, weight - 1, -1):
        dp[j] = max(dp[j], dp[j - weight] + value)

print(dp[k])
