def solution():
    n,m = map(int,input().split())
    person = [x+1 for x in range(n)]
    pop_index = 0
    stack = []
    while person:
        pop_index += m-1
        if n<=pop_index:
            pop_index%=n
        stack.append(person[pop_index])
        person.pop(pop_index)
        n-=1
    print("<"+", ".join(map(str,stack))+">")
solution()