from random import randint

class Map:
    def __init__(self,res,mur,sol,scale):
        self.res = [res[0]//10,res[1]//10]
        self.mur = mur
        self.sol = sol
        self.carte = [[randint(0,1) for i in range(self.res[0])] for i in range(self.res[1])]
        print(len(self.carte),len(self.carte[0]))
        self.carte[0][0] = 0

    
