#IMPORT
import pygame

#CLASS
class Monster:
    """
    CLASS MONSTER

    Cet objet est le monstre du jeu.
    A partir d'un certain temps, il apparait sur la carte
    et suit le joueur.
    Pour pouvoir suivre le joueur, il suit un algorithme :
        - save_player_location est une file avec toutes las cases
          où le joueur à marché 
          - si le joueur repasse sur la même case, il supprime celles d'avant 
            pour pas que le monstre ne fasse un détour
        - à chaque frame, il se déplace vers le point le plus proche de lui
          et si il l'atteint on le supprime de la file
    """
    def __init__(self,x,y,speed,sprite,start,scale):
        self.x, self.y = x, y
        self.speed = speed
        self.sprite = sprite
        self.save_player_location = []
        self.start = start
        self.coll = pygame.Rect(self.x,self.y,40,40)
        self.scale = scale
    
    def new_location(self,x,y):
        #ajoute la nouvelle position du joueur dans la file
        if (x,y) not in self.save_player_location:
            self.save_player_location.append((x,y))
        elif self.save_player_location[-1] != (x,y):
            while self.save_player_location[-1] != (x,y):
                self.save_player_location.pop(-1)
    
    def check_pos(self):
        #vérifie si le monstre est sur une case de la file et la supprime
        #sinon il se déplace ver sla case la plus proche
        if len(self.save_player_location) != 0:
            if (self.x//self.scale,self.y//self.scale) == self.save_player_location[0]:
                self.save_player_location.pop(0)
            if self.y//self.scale == self.save_player_location[0][1]:
                if self.x//self.scale <= self.save_player_location[0][0]:
                    self.x += self.speed
                else:
                    self.x -= self.speed
            else:
                if self.y//self.scale <= self.save_player_location[0][1]:
                    self.y += self.speed
                else:
                    self.y -= self.speed                

    def update_monster(self):
        #met à jour la box de collision du monstre
        self.coll = pygame.Rect(self.x,self.y,40,40)
