# 입력 받기
N = int(input())
arr = list(map(int, input().split()))
M = int(input())

# 팰린드롬 여부를 저장할 DP 테이블
dp = [[False] * N for _ in range(N)]

# 길이가 1인 부분 배열은 항상 팰린드롬
for i in range(N):
    dp[i][i] = True

# 길이가 2인 부분 배열
for i in range(N - 1):
    if arr[i] == arr[i + 1]:
        dp[i][i + 1] = True

# 길이가 3 이상인 부분 배열
for length in range(3, N + 1):  # 길이
    for start in range(N - length + 1):
        end = start + length - 1
        if arr[start] == arr[end] and dp[start + 1][end - 1]:
            dp[start][end] = True

# 결과를 저장할 리스트
results = []

# M개의 질문 처리
for _ in range(M):
    S, E = map(int, input().split())
    # S와 E는 1-indexed이므로 0-indexed로 변환
    if dp[S - 1][E - 1]:
        results.append(1)
    else:
        results.append(0)

# 결과 출력
for result in results:
    print(result)
