import pygame

class Monster:
    def __init__(self,x,y,speed,sprite,start,scale):
        self.x, self.y = x, y
        self.speed = speed
        self.sprite = sprite
        self.save_player_location = []
        self.start = start
        self.coll = pygame.Rect(self.x,self.y,40,40)
        self.scale = scale
    
    def new_location(self,x,y,coll_list):
        if (x,y) not in self.save_player_location and (x,y) not in coll_list:
            self.save_player_location.append((x,y))
        elif self.save_player_location[-1] != (x,y):
            while self.save_player_location[-1] != (x,y):
                self.save_player_location.pop(-1)
    
    def check_pos(self):
        if len(self.save_player_location) != 0:
            print(self.save_player_location)
            if (self.x//self.scale,self.y//self.scale) == self.save_player_location[0]:
                self.save_player_location.pop(0)
            if self.y == self.save_player_location[0][1]:
                if self.x <= self.save_player_location[0][0]:
                    self.x += self.speed
                else:
                    self.x -= self.speed
            else:
                if self.y <= self.save_player_location[0][1]:
                    self.y += self.speed
                else:
                    self.y -= self.speed                

    def update_monster(self):
        self.coll = pygame.Rect(self.x,self.y,40,40)
