import pygame

class Player:
    def __init__(self,x,y,sprite,speed):
        self.x = x
        self.y = y
        self.sprite = sprite
        self.coll = pygame.Rect(300,200,100,100)
        self.speed = speed

    def move_up(self) : self.y -= self.speed
    def move_down(self) : self.y += self.speed
    def move_left(self) : self.x -= self.speed
    def move_right(self) : self.x += self.speed


