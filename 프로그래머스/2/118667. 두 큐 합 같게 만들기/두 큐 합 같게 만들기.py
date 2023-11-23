def solution(queue1, queue2):
    answer = -2
    all_que = queue1+ queue2
    all_sum = sum(all_que)
    if all_sum%2!=0:
        return -1
    target = all_sum//2
    start,end = 0, len(queue1)
    target_sum = sum(queue1)
    max_len = len(all_que)
    for i in range(2*len(all_que)):
        if target == target_sum:
            return i
        if target < target_sum:
            if max_len<=start:
                break
            target_sum -= all_que[start]
            start+=1
        else:
            if max_len<=end:
                break
            target_sum += all_que[end]
            end +=1
        
    return -1