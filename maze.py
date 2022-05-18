from random import randrange,shuffle


class Maze:
    def __init__(self,w,h):
        self.w = w
        self.h = h
        self.maze = self.grid()
        self.wall, self.ground = self.wall_ground_list()


    def grid(self):
        grid = []
        nb_list = [i for i in range(self.w*self.h)]
        for i in range(self.h):
            l = []
            for j in range(self.w):
                if i%2 != 0 and j%2 != 0:
                    l.append(nb_list.pop(0))
                else:
                    l.append(-1)
            grid.append(l)
        return grid
    
    def wall_ground_list(self):
        wall = []
        ground = []
        for i in range(self.h):
            for j in range(self.w):
                if self.maze[i][j] == -1:
                    wall.append((i,j))
                else:
                    ground.append((i,j)) 
        return wall,ground

    def check_nb(self):
        n = self.maze[self.ground[0][0]][self.ground[1][0]]
        for g in self.ground:
            if self.maze[g[0]][g[1]] != n:
                return False
        return True

    def edit_nb(self,nb1,nb2):
        for i in range(self.h):
            for j in range(self.w):
                if self.maze[i][j] == nb2:
                    self.maze[i][j] = nb1


    def affiche(self):
        for i in range(self.h):
            l = ""
            for j in range(self.w):

                if self.maze[i][j] == -1:

                    l += "X "
                else: 
                    l += str(self.maze[i][j])+" "
            print(l)

    def gen_maze(self):
        while not self.check_nb():
            self.wall, self.ground = self.wall_ground_list()
            w = self.wall[randrange(len(self.wall))]
            #haut bas
            if w[0] > 0 and w[0] < self.h-1 and self.maze[w[0]-1][w[1]] != -1 and self.maze[w[0]+1][w[1]] != -1 and self.maze[w[0]-1][w[1]] != self.maze[w[0]+1][w[1]]:
                self.edit_nb(self.maze[w[0]-1][w[1]],self.maze[w[0]+1][w[1]])
                self.maze[w[0]][w[1]] = self.maze[w[0]-1][w[1]]
            #gauche droite
            if w[1] > 0 and w[1] < self.w-1 and self.maze[w[0]][w[1]-1] != -1 and self.maze[w[0]][w[1]+1] != -1 and self.maze[w[0]][w[1]-1] != self.maze[w[0]][w[1]+1]:
                self.edit_nb(self.maze[w[0]][w[1]-1],self.maze[w[0]][w[1]+1])
                self.maze[w[0]][w[1]] = self.maze[w[0]][w[1]-1]   
        for i in range(self.h):
            for j in range(self.w):
                if self.maze[i][j] == -1:
                    self.maze[i][j] = False
                else:
                    self.maze[i][j] = True
        return self.maze

