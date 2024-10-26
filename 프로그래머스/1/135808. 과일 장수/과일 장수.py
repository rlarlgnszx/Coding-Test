def solution(k, m, score):
    answer = 0
    # 사과 상태 1~k 점
    # 한상자에 사과 m개 포장
    # 상자중 낮은 점수가 p인 경우 사과 한상자 = p*m
    score.sort()
    n = len(score)
    count = n%m 
    ans = 0
    for i in range(count,n,m):
        ans += score[i]*m
    return ans