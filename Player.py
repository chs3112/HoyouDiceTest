import random as rd
from Tile_Map import Map, Tile

class Player:
    #생성자
    def __init__(self, sequence:int, game):
        self.sequence = sequence
        self.location = sequence*10;   
        self.tile: Tile = Map.tiles[self.location]
        self.tile.player = self;
        self.point = 0
        self.is_reStart = False
        self.game = game
        
    # main
    def TurnStart(self):
        self.RollDice()
        
        
    # main
    def RollDice(self):
        self.dice = rd.randrange(1,7)
        self.Moves(self.dice)
        
    # main
    def Moves(self, dice):
        self.MoveStart()
        for i in range(dice):
            self.PrePass()
            self.Move()
            self.PostPass()
        self.Arrival()
        
    def MoveStart(self):
        self.tile.player = None
        
        
    def Move(self):
        self.AddLocation(1)
        
    def PrePass(self):
        pass
    
    def PostPass(self):
        if self.location == self.sequence*10:
            self.AddPoint(1)
    
    
    # main
    def Arrival(self):
        self.tile = Map.tiles[self.location]
        if Map.tiles[self.location].Is_Special():
            self.is_reStart = True
        if Map.tiles[self.location].Is_ExistPlayer():
            self.Attack();
        self.tile.player = self
        self.TurnEnd()
        
    # main
    def TurnEnd(self):
        if self.is_reStart:
            self.ReStart()
        else:
            self.game.Next(self.sequence)
            
    def Attack(self):
        self.tile.player.Die()
        self.AddPoint(1)
            
    def Die(self):
        self.tile.player = None
        self.location = self.sequence*10
        self.tile = Map.tiles[self.location]
        self.AddPoint(-1)
        
    def ReStart(self):
        self.is_reStart = False
        self.RollDice()
        
    
    def AddLocation(self, num):
        self.location += num
        self.location -= 40 if self.location >= 40 else 0
        
    def AddPoint(self, num):
        self.point += num
        if self.point < 0:
            self.point = 0
        
        