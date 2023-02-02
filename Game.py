from Player import Player
from typing import List



def Create_Player(game):
    players:List[Player] = [Player(i, game) for i in range(4)]
    
    return players

class Save:
    n_rollDice = [0,0,0,0]
    n_Attack = [0,0,0,0]
    point = [0,0,0,0]
    n_travel_distance = [0,0,0,0]
    n_die = [0,0,0,0]

    
    @staticmethod
    def nprint():
        for i in range(4):
            print(f"{i}\n굴린 횟수 : {Save.n_rollDice[i]/100}\
                \n공격 횟수 : {Save.n_Attack[i]/100}\
                \n획득 점수 : {Save.point[i]/100}\
                \n이동 거리 : {Save.n_travel_distance[i]/100}\
                \n죽은 횟수 : {Save.n_die[i]/100}")


class Game:
    def __init__(self):
        self.turn = 0
        self.players:List[Player] = Create_Player(self)
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
        for i in range(4):
            Save.n_rollDice[i] += self.players[i].n_rollDice
            Save.n_Attack[i] += self.players[i].n_attack
            Save.point[i] += self.players[i].point
            Save.n_travel_distance[i] += self.players[i].n_travel_distance
            Save.n_die[i] += self.players[i].n_die
            

def main():
    for i in range(100):
        Game()
    Save.nprint()
        


if __name__ == '__main__':
    main()