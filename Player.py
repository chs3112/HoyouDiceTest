class Player:
    #생성자
    def __init__(self, sequence):
        self.sequence = sequence
        self.location = sequence*10;
        self.point = 0
        self.is_reStart = False
        
    
    def TurnStart(self):
        self.RollDice()
        
        
    def RollDice(self):
        self.dice = rd.randrange(1,7)
        self.Moves(self.dice)
        
    def PrePass():
        pass
        
    def Moves(self, dice):
        for i in range(dice):
            self.Move()
    
    
    def Arrival(self):
        if self.location%5==0:
            self.is_reStart = True
            
    def Move(self):
        self.AddLocation(1)
        
    def AddLocation(self, num):
        self.location += num
        self.location -= 40 if self.location >= 40 else 0
        
        