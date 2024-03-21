import sys
# 사람 n, 파티의 수 m
from collections import defaultdict

n,m = list(map(int,sys.stdin.readline().split()))#
# 진실아는 사람, 개수만큼 사람들 번호 
know_person = list(map(int,sys.stdin.readline().split()))[1:]
parent = [x for x in range(n+1)]

def find(x):
    if parent[x]!= x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a,b):
    a = find(a)
    b = find(b)
    if a in know_person and b in know_person:
        return 
    elif a in know_person:
        parent[b] = a
    elif b in know_person:
        parent[a] = b
    else:
        if a<b:
            parent[b]=a
        else:
            parent[a]=b

# for per in know_person:
    
new_party = []
for party in range(m):
    temp = list(map(int,sys.stdin.readline().split()))
    n = temp.pop(0)
    for par in range(n-1):
        union(temp[par],temp[par+1])
    new_party.append(temp)

# print(new_party)
ans = 0
for new in new_party:
    for person in new:
        if find(person) in know_person:
            break
    else:
        ans+=1
print(ans)