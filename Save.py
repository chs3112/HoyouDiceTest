import csv
from typing import List
import pandas as pd

class Save:
    repeat = 0
    columnn = ['n_rolled', 'n_attack', 'n_point', 'n_move', 'n_die']
    
    df = pd.DataFrame({'n_rolled':[0,0,0,0],
                           'n_attack':[0,0,0,0],
                           'n_point':[0,0,0,0],
                           'n_move':[0,0,0,0],
                           'n_die':[0,0,0,0]},
                      columns=columnn)
    
    @staticmethod
    def DataSave(n_rollDice: List[int], n_attack: List[int], point: List[int], n_travel_distance: List[int], n_die: List[int]):
        for i in range(4):
            Save.df.loc[i, 'n_rolled'] +=n_rollDice[i]
            Save.df.loc[i, 'n_attack'] +=n_attack[i]
            Save.df.loc[i, 'n_point'] +=point[i]
            Save.df.loc[i, 'n_move'] +=n_travel_distance[i]
            Save.df.loc[i, 'n_die'] +=n_die[i]
        

    
    @staticmethod
    def nprint():
        
        
        Save.df = Save.df.div(Save.repeat).round(2)
            
            
        Save.df.to_csv('Result.csv')

