from Tile_Map import Tile, Map
from Player import Player
from typing import List


def Create_Player():
    players:List[Player] = [Player(i) for i in range(4)]
    
    return players


class Game:
    def __init__(self):
        self.turn = 0
        self.players:List[Player] = Create_Player()
        self.Start()
        
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
        print("gameEnd")
            

def main():
    Game()


if __name__ == '__main__':
    main()