from Player import Player
from typing import List



def Create_Player(game):
    players:List[Player] = [Player(i, game) for i in range(4)]
    
    return players

class Save:
    repeat = 0
    n_rollDice = [0,0,0,0]
    n_Attack = [0,0,0,0]
    point = [0,0,0,0]
    n_travel_distance = [0,0,0,0]
    n_die = [0,0,0,0]
    error = 0

    
    @staticmethod
    def nprint():
        for i in range(4):
            print(f"{i}\n굴린 횟수 : {Save.n_rollDice[i]/Save.repeat}\
                \n공격 횟수 : {Save.n_Attack[i]/Save.repeat}\
                \n획득 점수 : {Save.point[i]/Save.repeat}\
                \n이동 거리 : {Save.n_travel_distance[i]/Save.repeat}\
                \n죽은 횟수 : {Save.n_die[i]/Save.repeat}")
        print(f"오류 : {Save.error}")


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
        if sum(Save.n_Attack) != sum(Save.n_die):
            Save.error += 1;
        for i in range(4):
            Save.n_rollDice[i] += self.players[i].n_rollDice
            Save.n_Attack[i] += self.players[i].n_attack
            Save.point[i] += self.players[i].point
            Save.n_travel_distance[i] += self.players[i].n_travel_distance
            Save.n_die[i] += self.players[i].n_die
            

def main():
    Save.repeat = int(input("반복 횟수 : "))
    for i in range(Save.repeat):
        Game()
    Save.nprint()
        


if __name__ == '__main__':
    main()