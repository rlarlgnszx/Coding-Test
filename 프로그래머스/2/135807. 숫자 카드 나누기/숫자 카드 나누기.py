from math import gcd
from functools import reduce
def can_divide(array, value):
    return all(num % value != 0 for num in array)

def solution(arrayA, arrayB):
    answer = 0
    a = reduce(gcd,arrayA)
    b = reduce(gcd,arrayB)
    
    if b>1 and all(num % b != 0 for num in arrayA):
        answer = b
    if a>1 and all(num % a != 0 for num in arrayB):
        answer = max(answer,a)
    
    return answer