want = int(input())
n = int(input())
have = set()
if n !=0:
    have = set(map(int,input().split()))
# have = list(map(str,have))

min_count = abs(100-int(want))
for nums in range(1000001):
    nums = str(nums)
    
    for j,cha in enumerate(nums):
        if int(cha) in have:
            break

        elif j == len(nums)-1:
            min_count = min(min_count,abs(want-int(nums))+len(nums))

print(min_count)