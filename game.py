import pygame
from player import Player
from map import Map
from random import randrange
class Game:
    def __init__(self, res, scale):
        self.res = res
        self.scale = scale
        self.screen = pygame.display.set_mode(res)
        self.running = True 
        self.clock = pygame.time.Clock()
        self.player = Player(300,200,(255,0,0),2)
        self.map = Map(self.res,(0,255,0),(0,0,255),self.scale)
        self.map.walk(randrange(self.map.res[0]),randrange(self.map.res[1]))
        print("fin")
        self.map.carte[20][30] = True
        print(self.map.carte)


    def handle_inputs(self,player):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_z]:
            player.move_up()  
        elif pressed[pygame.K_s]:
            player.move_down()  
        elif pressed[pygame.K_q]:
            player.move_left() 
        elif pressed[pygame.K_d]:
            player.move_right() 

    def draw_map(self,scale):
        wall_coll = []
        for i in range(40):
            for j in range(60):
                if not self.map.carte[i][j]:
                    wall_coll.append(pygame.Rect(j*scale,i*scale,scale,scale))
                    pygame.draw.rect(self.screen,self.map.mur,pygame.Rect(j*scale,i*scale,scale,scale))
                else:
                    pygame.draw.rect(self.screen,self.map.sol,pygame.Rect(j*scale,i*scale,scale,scale))
        return wall_coll

    def check_coll(self,col):
        for collision in col:
            if self.player.coll.colliderect(collision):
                return True
        return False

    def update(self):
        self.screen.fill((0,0,0))
        coll_list = self.draw_map(self.scale)
        x,y = self.player.x,self.player.y
        self.handle_inputs(self.player)
        self.player.update_player()
        if self.check_coll(coll_list):
            self.player.x = x
            self.player.y = y
        self.player.update_player()   
        pygame.draw.rect(self.screen,self.player.sprite,self.player.coll)

    def run(self):
        while self.running:
            self.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            pygame.display.flip()
            self.clock.tick(60)

