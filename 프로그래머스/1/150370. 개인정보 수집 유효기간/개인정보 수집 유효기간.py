import re
from heapq import heappop, heappush
def solution(today, terms, privacies):
    answer = []
    max_days=28
    max_month=12
    start_year =2000
    terms_plus ={}
    for i in terms:
        a,b = i.split(' ')
        b = int(b)*28
        terms_plus[a]=b
    y,m,d = list(map(int,today.split('.')))
    today = (y-2000)*12*28 + m*28 + d
    index = 1
    
    for i in privacies:
        year,typ = i.split(' ')
        y,m,d = list(map(int,year.split('.')))
        checking = (y-2000)*12*28 + m*28 + d + terms_plus[typ]
        if today>checking-1:
            answer.append(index)
        index+=1
        
    return answer