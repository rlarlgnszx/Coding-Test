from itertools import combinations,permutations
def solution():
    n = int(input())
    board= []
    for j in range(n):
        board.append(list(map(int,input().split())))
    person = set(x for x in range(n))
    start_team = list(combinations(person,int(n/2)))
    result = 'None'
    for j in start_team:
        start = set(j)
        link = person-start
        real_start=  list(permutations(start,2))
        real_link= list(permutations(link,2))
        result_x,result_y = 0,0
        for x,y in zip(real_start,real_link):
            result_x+=board[x[0]][x[1]]
            result_y+=board[y[0]][y[1]]
        if result =='None':
            result = abs(result_x-result_y)
        else:
            t = abs(result_x-result_y)
            result = min(t,result)
    print(result)
        
solution()
    