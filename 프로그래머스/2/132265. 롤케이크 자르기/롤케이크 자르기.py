from collections import Counter
def solution(topping):
    answer = 0
    n = len(topping)
    fi = Counter([topping[0]])
    se = Counter(topping[1:])
    cut_i  =1
    while cut_i!=n:
        next = topping[cut_i]
        fi[next]+=1
        se[next]-=1
        if se[next]==0:
            del se[next]
        if len(fi)==len(se):
            answer+=1
        cut_i+=1
    return answer