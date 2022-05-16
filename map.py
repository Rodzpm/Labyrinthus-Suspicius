from random import shuffle, randrange

class Map:
    def __init__(self,res,mur,sol,scale):
        self.res = [res[0]//20,res[1]//20]
        self.mur = mur
        self.sol = sol
        self.vis = [[0] * self.res[0] + [1] for _ in range(self.res[1])] + [[1] * (self.res[0] + 1)]
        self.ver = [[True] * self.res[0] + [True] for _ in range(self.res[1])] + [[]]
        self.hor = [[True] * self.res[0] + [True] for _ in range(self.res[1] + 1)]
    def make_maze(self):
        def walk(x, y):
            self.vis[y][x] = 1
            d = [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]
            shuffle(d)
            for (xx, yy) in d:
                if self.vis[yy][xx]: continue
                if xx == x: self.hor[max(y, yy)][x] = False
                if yy == y: self.ver[y][max(x, xx)] = False
                walk(xx, yy)
    
        walk(randrange(self.res[0]), randrange(self.res[1]))
        s = []
        for (a, b) in zip(self.hor, self.ver):
            s += a,b
        return s

