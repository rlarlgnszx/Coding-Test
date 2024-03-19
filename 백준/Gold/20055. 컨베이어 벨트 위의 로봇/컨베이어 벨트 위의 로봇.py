# 돈다
# n + n 
# 1 번 -> 올리는 , n번 => 내리는 위치
# 올리거나 ,로봇이 이동하면 내구도 1감소

# 목표 : 컨베이어 벨트로 로봇들을 반대편으로 옮긴다.
## 일의 순서
# 각 칸 위에 로봇과 함께 한칸 회전
# 벨트에 올라간 로봇부터 , 벨트가 회전하는 방향으로 1칸이동할수있으면 이동
# 1. 로봇이 이동하려면 로봇이 없어야하며 내구도있어어ㅑ한다.
# 3. 올리는 위치에 내구도 0이 아니면 로봇올림
# 내구도 0인 칸 개수 k라면 종료 , 아니면 1로 돌아감
n, k= map(int,input().split())
class container_runner:
    def __init__(self) -> None:
        self.board = [[int(x),False] for x in input().split()]
        self.start = 0
        self.container = len(self.board)
        self.end = self.container//2-1
        self.k_count = 0

    def step1(self):
    # 벨트 회전
        self.start -=1
        if self.start <0 :
            self.start = self.container-1
        self.end -=1
        if self.end <0 :
            self.end = self.container-1
    # 이동하려는 칸에 로봇이 없으며, 내구도 1이상인것
        if self.board[self.end][1]==True:
            self.board[self.end][1]=False
        
    def step2(self):
        # list 내에서 -> 
        if self.start < self.end:
            for i in range(self.end,self.start-1,-1):
                if self.board[i][1]==True and self.board[i+1][1]==False and self.board[i+1][0]>0:
                    self.board[i][1]=False
                    
                    self.board[i+1][1]=True
                    self.board[i+1][0]-=1
                    if self.board[i+1][0]==0:
                        self.k_count+=1
        else:
            for i in range(self.end,-1,-1):
                if self.board[i][1]==True and self.board[i+1][1]==False and self.board[i+1][0]>0:
                    self.board[i][1]=False
                    
                    self.board[i+1][1]=True
                    self.board[i+1][0]-=1
                    if self.board[i+1][0]==0:
                        self.k_count+=1
            
            if self.board[self.container-1][1]==True and self.board[0][1]==False and self.board[0][0]>0:
                self.board[self.container-1][1]=False
                self.board[0][1]=True
                self.board[0][0]-=1
                if self.board[0][0]==0:
                    self.k_count+=1
            
            for i in range(self.container-2,self.start-1,-1):
                # print(self.start,self.end,i)
                if self.board[i][1]==True and self.board[i+1][1]==False and self.board[i+1][0]>0:
                    self.board[i][1]=False
                    self.board[i+1][1]=True
                    self.board[i+1][0]-=1
                    if self.board[i+1][0]==0:
                        self.k_count+=1         
                            
        if self.board[self.end][1]==True:
            self.board[self.end][1]=False

    def step3(self):
        if self.board[self.start][1] == False and self.board[self.start][0]>0:
            self.board[self.start][0]-=1
            if self.board[self.start][0]==0:
                    self.k_count+=1
            self.board[self.start][1]=True
        
        
    def step4(self):
        if self.k_count>=k:
            return True
        return False

    def print_board(self):
        print(self.board)
ans = 0
c = container_runner()

while 1:
    ans +=1
    # print("step1 : \n")
    c.step1()
    # c.print_board()
    
    # print("step2 : \n")
    c.step2()
    # c.print_board()
    
    # print("step3: \n")
    c.step3()
    # c.print_board()
    
    if c.step4():
        print(ans)
        break

    
    
# 투포인터 사용하고 self.board를 이중리스트로 사용해 내구도,로봇존재 로사용
