import sys
from collections import deque

input = sys.stdin.readline

# 방향 정의 (상, 하, 좌, 우)
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def is_valid(x, y):
    return 0 <= x < R and 0 <= y < C

# 보드 크기 입력
R, C = map(int, input().split())
board = [input().strip() for _ in range(R)]

# BFS 초기화
max_count = 0
# 큐에 (x, y, 방문 비트 마스크, 거리) 추가
queue = deque([(0, 0, 1 << (ord(board[0][0]) - ord('A')), 1)])  # 시작 문자 비트 마스크 초기화
visited_states = set()  # 방문한 상태를 저장할 집합

while queue:
    x, y, visited_mask, dist = queue.popleft()
    max_count = max(max_count, dist)

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if is_valid(nx, ny):
            next_char = board[nx][ny]
            char_bit = 1 << (ord(next_char) - ord('A'))  # 해당 문자의 비트 위치
            
            if not (visited_mask & char_bit):  # 해당 문자가 방문하지 않은 경우
                new_visited_mask = visited_mask | char_bit  # 비트 마스크 업데이트
                
                # 새로운 상태가 방문한 적이 없는 경우에만 큐에 추가
                if (nx, ny, new_visited_mask) not in visited_states:
                    visited_states.add((nx, ny, new_visited_mask))
                    queue.append((nx, ny, new_visited_mask, dist + 1))

print(max_count)
