def solution(storey):
    answer = 0
    while storey > 0:
        remainder = storey % 10
        if remainder > 5 or (remainder == 5 and (storey // 10) % 10 >= 5):
            answer += (10 - remainder)
            storey += 10
        else:
            answer += remainder
        storey //= 10
    return answer