import sys
from collections import deque
input =sys.stdin.readline

n,m = map(int,input().split())
max_pos = 100000

visited= [int(1e9)]*(max_pos+1)
visited[n] = 0
count= [0]*(max_pos+1)
count[n]=1
que = deque([n])
while que:
    cur =que.popleft()
    if cur-1>=0 and visited[cur]+1 <= visited[cur-1]:
        if visited[cur]+1 == visited[cur-1]:
            count[cur-1] += count[cur]
        else:
            visited[cur-1] = visited[cur] + 1
            count[cur-1] = count[cur]
            que.append(cur-1)
    if cur+1<=max_pos and visited[cur]+1 <= visited[cur+1]:
        if visited[cur]+1 == visited[cur+1] :
            count[cur+1] += count[cur]
        else:
            visited[cur+1] = visited[cur] +1
            count[cur+1] = count[cur]
            que.append(cur+1)
    if cur*2<=max_pos and visited[cur]+1 <= visited[cur*2]:
        if visited[cur]+1 == visited[cur*2] :
            count[cur*2] += count[cur]
        else:
            visited[cur*2] = visited[cur]+1
            count[cur*2] = count[cur]
            que.append(cur*2)

print(visited[m])
print(count[m])