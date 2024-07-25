import sys
from collections import deque
input = sys.stdin.readline

a = deque(input().rstrip())
b = list(input().rstrip())
k = len(b)
stack = []

while a or stack:  # a가 비거나 stack이 비어있지 않을 때까지 반복
    if len(stack) >= k and stack[-k:] == b:  # stack의 길이가 k 이상일 때만 비교
        del stack[-k:]  # b와 일치하면 k개를 제거
    elif a:  # a가 남아있으면
        stack.append(a.popleft())  # stack에 문자 추가
    else:
        break  # a가 비면 종료

if stack:
    print("".join(stack))
else:
    print("FRULA")