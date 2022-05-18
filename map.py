from random import shuffle, randrange
from maze import Maze
class Map:
    def __init__(self,res,mur,sol,tp):
        self.res = [res[0]//40,res[1]//40]
        self.mur = mur
        self.sol = sol
        self.tp = tp
        self.map = Maze(self.res[0],self.res[1])
        self.maze = self.map.gen_maze()
        
    

