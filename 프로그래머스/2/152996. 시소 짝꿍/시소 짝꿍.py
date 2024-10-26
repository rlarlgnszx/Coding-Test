from collections import Counter

def solution(weights):
    weight_count = Counter(weights)
    answer = 0
    
    # 1. 동일한 몸무게 쌍 계산
    for weight, count in weight_count.items():
        if count > 1:
            answer += count * (count - 1) // 2

    # 2. 다른 몸무게 쌍 계산
    distance_ratios = [2/3, 3/4, 1/2]
    
    for weight in weight_count:
        for ratio in distance_ratios:
            pair_weight = weight * ratio
            if pair_weight in weight_count:
                answer += weight_count[weight] * weight_count[pair_weight]
                
    return answer