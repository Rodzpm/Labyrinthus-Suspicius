from random import randint

from random import shuffle
class Map:
    def __init__(self,res,mur,sol,scale):
        self.res = [res[0]//10,res[1]//10]
        self.mur = mur
        self.sol = sol
        self.carte = [[False] * self.res[0] for i in range(self.res[1])]
    def walk(self,x,y):
        self.carte[y][x] = True
        d = [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]
        shuffle(d)
        for (xx,yy) in d:
            if randint(0,1) == 1 and xx >= 0 and xx < self.res[0] and yy >= 0 and yy < self.res[1] and not self.carte[yy][xx]:
                self.walk(xx,yy)
        self.carte[0] = [False] * self.res[0]
        self.carte[-1] = [False] * self.res[0]
        for i in range(self.res[1]):
            self.carte[i][0] = False
            self.carte[i][-1] = False


    
