import sys
from itertools import combinations
from collections import deque

input = sys.stdin.readline

# 방향 정의 (상, 하, 좌, 우)
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def is_valid(x, y):
    return 0 <= x < N and 0 <= y < M

def spread_virus(lab):
    queue = deque()
    for i in range(N):
        for j in range(M):
            if lab[i][j] == 2:
                queue.append((i, j))
    
    while queue:
        x, y = queue.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if is_valid(nx, ny) and lab[nx][ny] == 0:
                lab[nx][ny] = 2  # 바이러스가 퍼짐
                queue.append((nx, ny))

def count_safe_area(lab):
    return sum(row.count(0) for row in lab)

N, M = map(int, input().split())
original_lab = [list(map(int, input().split())) for _ in range(N)]

empty_spaces = [(i, j) for i in range(N) for j in range(M) if original_lab[i][j] == 0]

max_safe_area = 0

# 빈 공간에서 3개의 벽을 세우는 모든 조합
for walls in combinations(empty_spaces, 3):
    # 벽을 세운 실험실 복사
    lab = [row[:] for row in original_lab]
    
    for (x, y) in walls:
        lab[x][y] = 1  # 벽 세우기
    
    # 바이러스 확산
    spread_virus(lab)
    
    # 안전 영역 계산
    safe_area = count_safe_area(lab)
    max_safe_area = max(max_safe_area, safe_area)

print(max_safe_area)
