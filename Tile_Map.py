from typing import List

class Tile:
    def __init__(self, sequence):
        self.sequence = sequence
        self.player = None
        self.is_Special = True if sequence%5 == 0 else False
        
    def Is_Special(self):
        return self.is_Special
    
    def Is_ExistPlayer(self):
        return False if self.player == None else True

class Map:
    tiles:List[Tile] = [Tile(i) for i in range(40)]
