import pygame

class Player:
    def __init__(self,x,y,sprite,speed):
        self.x = x
        self.y = y
        self.sprite = sprite
        self.coll = pygame.Rect(self.x+10,self.y+10,20,20)
        self.speed = speed
        self.is_sprint = False
        #Up:0, Down:1, Left:2, Right:3
        self.orientation = 1

    def move_up(self) : 
        self.y -= self.speed 
        self.orientation = 0
    def move_down(self) : 
        self.y += self.speed
        self.orientation = 1
    def move_left(self) : 
        self.x -= self.speed
        self.orientation = 2
    def move_right(self) : 
        self.x += self.speed
        self.orientation = 3

    def update_player(self):
        self.coll = pygame.Rect(self.x+10,self.y+10,20,20)

