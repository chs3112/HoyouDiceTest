from Player import Player
from typing import List
from Tile_Map import Map
from Save import Save


class Game:
    def __init__(self):
        self.turn = 0
        self.players:List[Player] = self.Create_Player(self)
        Map.SetTile()
        self.Start()
        
    def Create_Player(self, game):
        players:List[Player] = [Player(i, game) for i in range(4)]
        
        return players
        
    def Start(self):
        self.players[0].TurnStart();
        
    def Next(self, prePlayer):
        self.postPlayer = prePlayer+1
        if self.postPlayer == 4:
            self.postPlayer = 0
            self.turn += 1;
            if self.turn == 10:
                self.GameEnd()
                return
        self.players[self.postPlayer].TurnStart();
        
    def GameEnd(self):
        n_rollDice = [self.players[i].n_rollDice for i in range(4)]
        n_attack = [self.players[i].n_attack for i in range(4)]
        point = [self.players[i].point for i in range(4)]
        n_travel_distance = [self.players[i].n_travel_distance for i in range(4)]
        n_die = [self.players[i].n_die for i in range(4)]
        Save.DataSave(n_rollDice, n_attack, point, n_travel_distance, n_die)
        
            

def main():
    Save.repeat = int(input("반복 횟수 : "))
    for i in range(Save.repeat):
        Game()
    Save.nprint()
        


if __name__ == '__main__':
    main()