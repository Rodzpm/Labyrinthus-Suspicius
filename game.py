import pygame
from player import Player
from map import Map

class Game:
    def __init__(self, res, scale):
        self.res = res
        self.scale = scale
        self.screen = pygame.display.set_mode(res)
        self.running = True 
        self.clock = pygame.time.Clock()
        self.player = Player(30,20,(255,0,0),1)
        self.map = Map(self.res,(0,255,0),(0,0,255),self.scale)


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
        for i in range(4):
            for j in range(6):
                if self.map.carte[i-self.player.y-2][j-self.player.x-3] == 1:
                    pygame.draw.rect(self.screen,self.map.mur,pygame.Rect(j*scale,i*scale,scale,scale))
                else:
                    pygame.draw.rect(self.screen,self.map.sol,pygame.Rect(j*scale,i*scale,scale,scale))



    def update(self):
        self.screen.fill((0,0,0))
        self.draw_map(self.scale)
        self.handle_inputs(self.player)
        pygame.draw.rect(self.screen,self.player.sprite,self.player.coll)

    def run(self):
        while self.running:
            self.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            pygame.display.flip()
            self.clock.tick(60)

