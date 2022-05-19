#IMPORTS
from random import randrange,shuffle

#CLASS
class Maze:
    """
    CLASS MAZE 

    Cet objet créer un labyrinthe de manière aléatoire
    La méthode est la suivante :
        - créer une grille alternant mur et sol avec -1
          pour les murs et un nombre unique pour le sol
        - tant que le sol ne représente pas qu'un seul nombre
          continuer la boucle suivante :
            - prendre un mur aléatoire 
            - si les cellules que sépare le mur n'ont pas le
              même nombre, retirer le mur et mettre les cellules
              au même nombre
    Cette méthode permet d'avoir un labyrinthe aléatoire 
    """
    def __init__(self,w,h):
        self.w = w
        self.h = h
        self.maze = self.grid()
        self.wall, self.ground = self.wall_ground_list()


    def grid(self):
        #créer une grille alternant murs, et sols
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
        #donne la liste des murs présents dans la grille
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
        #vérifie si le labyrinthe est complet
        n = self.maze[self.ground[0][0]][self.ground[1][0]]
        for g in self.ground:
            if self.maze[g[0]][g[1]] != n:
                return False
        return True

    def edit_nb(self,nb1,nb2):
        #fusionne deux cellules en une seule
        for i in range(self.h):
            for j in range(self.w):
                if self.maze[i][j] == nb2:
                    self.maze[i][j] = nb1

    def gen_maze(self):
        #tant que le labyrinthe n'est pas complet :
        while not self.check_nb():
            #on récupère tous les murs et on en choisi un au hasard
            self.wall, self.ground = self.wall_ground_list()
            w = self.wall[randrange(len(self.wall))]
            #si le mur sépare deux cellules en haut et en bas :
            if w[0] > 0 and w[0] < self.h-1 and self.maze[w[0]-1][w[1]] != -1 and self.maze[w[0]+1][w[1]] != -1 and self.maze[w[0]-1][w[1]] != self.maze[w[0]+1][w[1]]:
                self.edit_nb(self.maze[w[0]-1][w[1]],self.maze[w[0]+1][w[1]])
                self.maze[w[0]][w[1]] = self.maze[w[0]-1][w[1]]
            #si le mur sépare deux cellules à gauche et à droite :
            if w[1] > 0 and w[1] < self.w-1 and self.maze[w[0]][w[1]-1] != -1 and self.maze[w[0]][w[1]+1] != -1 and self.maze[w[0]][w[1]-1] != self.maze[w[0]][w[1]+1]:
                self.edit_nb(self.maze[w[0]][w[1]-1],self.maze[w[0]][w[1]+1])
                self.maze[w[0]][w[1]] = self.maze[w[0]][w[1]-1]   
        #on modifie les murs par des False et le sol par des True
        for i in range(self.h):
            for j in range(self.w):
                if self.maze[i][j] == -1:
                    self.maze[i][j] = False
                else:
                    self.maze[i][j] = True
        return self.maze

