#IMPORT 
from random import shuffle, randrange
from maze import Maze

#CLASS
class Map:
    """
    CLASS MAP

    Cet objet permet de définir la map du jeu ainsi que le labyrinthe
    
    """
    def __init__(self,res,mur,sol,tp):
        self.res = [res[0]//40,res[1]//40]
        self.mur = mur
        self.sol = sol
        self.tp = tp
        self.map = Maze(self.res[0],self.res[1])
        self.maze = self.map.gen_maze()
        
    

