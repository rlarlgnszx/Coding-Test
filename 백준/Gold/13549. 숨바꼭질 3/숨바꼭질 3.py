import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())

# 방문 시간을 기록할 배열
visited = [int(1e9)] * 100001
visited[n] = 0  # 수빈이의 시작 위치는 0초

# BFS를 위한 큐 초기화
queue = deque([n])

while queue:
    cur = queue.popleft()

    # 1. 걷기 (X + 1)
    if cur + 1 <= 100000 and visited[cur + 1] > visited[cur] + 1:
        visited[cur + 1] = visited[cur] + 1
        queue.append(cur + 1)

    # 2. 걷기 (X - 1)
    if cur - 1 >= 0 and visited[cur - 1] > visited[cur] + 1:
        visited[cur - 1] = visited[cur] + 1
        queue.append(cur - 1)

    # 3. 순간 이동 (2 * X)
    if cur * 2 <= 100000 and visited[cur * 2] > visited[cur]:
        visited[cur * 2] = visited[cur]
        queue.append(cur * 2)

# 동생의 위치 K에 도달하는 최소 시간을 출력
print(visited[k])
