def find_closest_solution(n, solutions):
    left = 0
    right = n - 1
    closest_sum = float('inf')
    best_pair = (0, 0)

    while left < right:
        current_sum = solutions[left] + solutions[right]
        
        # 현재 합계가 0에 가까운지 확인
        if abs(current_sum) < abs(closest_sum):
            closest_sum = current_sum
            best_pair = (solutions[left], solutions[right])

        # 합계가 0보다 작으면 왼쪽 포인터를 오른쪽으로 이동
        if current_sum < 0:
            left += 1
        # 합계가 0보다 크면 오른쪽 포인터를 왼쪽으로 이동
        else:
            right -= 1

    return best_pair

# 입력 처리
n = int(input())
solutions = list(map(int, input().split()))

# 특성값이 0에 가장 가까운 두 용액 찾기
result = find_closest_solution(n, solutions)

# 결과 출력 (오름차순으로 출력)
print(min(result), max(result))
