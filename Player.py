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
        self.is_origin_protection = True
        
        self.n_rollDice = 0
        self.n_attack = 0
        self.n_travel_distance = 0
        self.n_die = 0
        
    # main
    def TurnStart(self):
        self.is_origin_protection = False
        self.RollDice()
        
        
    # main
    def RollDice(self):
        self.n_rollDice += 1
        self.dice = rd.randrange(1,7)
        self.n_travel_distance += self.dice
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
        if self.tile.is_Special:
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
        if self.tile.player.Die():
            self.n_attack+= 1
            self.AddPoint(1)
            
    def Die(self):
        if not self.is_origin_protection:
            self.is_origin_protection = True
            self.n_die += 1
            self.tile.player = None
            self.location = self.sequence*10
            self.tile = Map.tiles[self.location]
            self.AddPoint(-1)
            return True
        else:
            return False
        
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
        
        