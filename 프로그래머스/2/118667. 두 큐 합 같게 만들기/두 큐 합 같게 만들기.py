def solution(queue1, queue2):
    # 두 큐의 합을 계산
    total = sum(queue1) + sum(queue2)
    
    # 총합이 홀수인 경우, 같은 합을 만들 수 없음
    if total % 2 != 0:
        return -1

    target = total // 2  # 목표 합
    combined = queue1 + queue2  # 두 큐를 연결
    length = len(combined)
    sum_current = sum(queue1)
    start, end = 0, len(queue1)  # 시작점과 끝점

    for count in range(2 * length):
        if sum_current == target:
            return count
        if sum_current > target:
            if start < length:
                sum_current -= combined[start]
                start += 1
        else:
            if end < length:
                sum_current += combined[end]
                end += 1
            else:
                break  # 리스트 범위를 벗어나면 반복 종료

    return -1

# # 예시 실행
# print(solution([3, 2, 7, 2], [4, 6, 5, 1]))  # 결과: 2
# print(solution([1, 2, 1, 2], [1, 10, 1, 2]))  # 결과: 7
# print(solution([1, 1], [1, 5]))  # 결과: -1
