from collections import deque, defaultdict

def count_nodes(graph, start, n):
    visited = [False] * (n + 1)
    queue = deque([start])
    visited[start] = True
    count = 0
    
    while queue:
        node = queue.popleft()
        count += 1
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
                
    return count

def solution(n, wires):
    min_difference = float('inf')
    
    # 각 간선을 하나씩 제거하여 네트워크를 분리
    for i in range(len(wires)):
        # 그래프 구성
        graph = defaultdict(list)
        for j, (v1, v2) in enumerate(wires):
            if i == j:  # 현재 간선을 제거
                continue
            graph[v1].append(v2)
            graph[v2].append(v1)
        
        # 두 네트워크의 노드 개수 세기
        nodes_in_first_part = count_nodes(graph, wires[i][0], n)
        nodes_in_second_part = n - nodes_in_first_part
        difference = abs(nodes_in_first_part - nodes_in_second_part)
        
        # 최소 차이 갱신
        min_difference = min(min_difference, difference)
    
    return min_difference
