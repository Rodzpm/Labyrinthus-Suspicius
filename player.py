#IMPORT
import pygame

#CLASS
class Player:
    """
    OBJET PLAYER

    Cet objet défini le joueur et modifie sa position
    en fonction des déplacements. 
    
    """
    def __init__(self,x,y,sprite,speed):
        #coordonées du joueur
        self.x = x
        self.y = y
        #sprite du joueur
        self.sprite = sprite
        #box de collision du joueur
        self.coll = pygame.Rect(self.x+10,self.y+10,20,20)
        #vitesse du joueur
        self.speed = speed
        #booleen sur l'action de sprint
        self.is_sprint = False
        #orientation du sprite selon les valeurs suivantes : Up:0, Down:1, Left:2, Right:3
        self.orientation = 1

    def move_up(self) : 
        #déplace le joueur vers le haut
        self.y -= self.speed 
        self.orientation = 0
    def move_down(self) : 
        #déplace le joueur vers le bas
        self.y += self.speed
        self.orientation = 1
    def move_left(self) : 
        #déplace le joueur vers la gauche
        self.x -= self.speed
        self.orientation = 2
    def move_right(self) : 
        #déplace le joueur vers la droite
        self.x += self.speed
        self.orientation = 3

    def update_player(self):
        #met à jour la box de collision du joueur
        self.coll = pygame.Rect(self.x+10,self.y+10,20,20)

