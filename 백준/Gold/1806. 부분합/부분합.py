import sys
input =sys.stdin.readline


n,s = map(int,input().split())

numbers = list(map(int,input().split()))
min_size =sys.maxsize

sum_numbers=  0
left,right = 0,0

while 1:
    if sum_numbers >= s:
        min_size = min(min_size,right-left)
        sum_numbers -= numbers[left]
        left +=1
        
    elif right==n:
        break
    else:
        sum_numbers+= numbers[right]
        right+=1
## dp i,j 는 i~부터 j까지의 최솟값


if min_size==sys.maxsize:
    print(0)
else:
    print(min_size)