def solution():
    check=['c=','c-','dz=','d-','lj','nj','s=','z=']
    inp = input()
    i= 0
    answer = 0
    while i<=len(inp)-1:
        # print(i)
        if i+3 <=len(inp) and inp[i:i+3] in check:
            # print(inp[i:i+3])
            i+=3
            answer +=1
        elif i+2 <=len(inp) and inp[i:i+2] in check:
            # print(inp[i:i+2])
            i+=2
            answer +=1
        else:
            answer +=1
            i+=1
    print(answer)
solution()
        
            
       