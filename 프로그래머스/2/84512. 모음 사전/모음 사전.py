def solution(word):
    li = ['A', 'E', 'I', 'O', 'U']
    global answer
    answer = 0
    def dfs(li,stri):
        global answer
        if stri==word:
            return True
        if len(stri)==5:
            return False
        for i in li:
            answer+=1
            c = dfs(li,stri+i)
            if c :
                return True
    dfs(li,"")
    return answer
