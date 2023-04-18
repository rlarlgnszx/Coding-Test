def solution():
    n = int(input())
    odd_check = 0
    if n==1:
        print("1/1")
        return
    n-=1
    sumit = 0
    for i in range(10_000_000):
        sumit+= i
        if sumit>n:
            odd_check = i%2
            sumit-=i
            break
    n-=sumit
    if odd_check: 
        left,right = i,1
        print(f'{left-n}/{right+n}')
    else:
        left,right = 1,i
        print(f'{left+n}/{right-n}')
# for i in range(1,10):
#     solution(i)
solution()