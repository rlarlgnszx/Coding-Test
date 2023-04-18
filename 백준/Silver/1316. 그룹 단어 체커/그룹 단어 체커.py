from collections import Counter
import sys
def solution():
    n = int(input())
    
    def group(s):
        c =Counter(s)
        before_word = None
        for i in s:
            if before_word==None:
                before_word=i
            if before_word==i and c[i]>=1:
                c[i]-=1
            else:
                return False
            if c[i]==0:
                before_word=None
        return True
    answer = 0
    
    for i in range(n):
        temp = group(sys.stdin.readline().rstrip())
        if temp:
            answer +=1
    print(answer)
solution()