from itertools import permutations
import re

def calculate(expression, ops):
    """계산 수행 함수"""
    # 연산자 우선순위에 따라 순차적으로 계산
    for op in ops:
        while op in expression:
            idx = expression.index(op)
            if op == '+':
                result = expression[idx - 1] + expression[idx + 1]
            elif op == '-':
                result = expression[idx - 1] - expression[idx + 1]
            else:
                result = expression[idx - 1] * expression[idx + 1]
            expression = expression[:idx - 1] + [result] + expression[idx + 2:]
    return expression[0]

def solution(expression):
    # 연산자 분리
    numbers = list(map(int, re.split(r'[\+\-\*]', expression)))
    operators = re.findall(r'[\+\-\*]', expression)

    # 모든 연산자 조합 생성
    all_combinations = list(permutations(set(operators), len(set(operators))))

    max_value = 0
    for ops in all_combinations:
        exp = []
        for num, op in zip(numbers, operators + ['']):
            exp.append(num)
            if op:
                exp.append(op)

        # 해당 우선순위로 계산
        result = abs(calculate(exp, ops))
        max_value = max(max_value, result)

    return max_value

# 테스트
# print(solution("100-200*300-500+20"))  # 60420
# print(solution("50*6-3*2"))  # 300

