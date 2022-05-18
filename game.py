import pygame
from player import Player
from map import Map
from random import randrange


class Game:
    def __init__(self, res, scale):
        self.res = res
        self.scale = scale
        self.screen = pygame.display.set_mode(res)
        self.player_sprite = [pygame.image.load("assets/sprites/Up_Carac.png").convert_alpha(),
                              pygame.image.load("assets/sprites/Down_Carac.png").convert_alpha(),
                              pygame.image.load("assets/sprites/Left_Carac.png").convert_alpha(),
                              pygame.image.load("assets/sprites/Right_Carac.png").convert_alpha()]
        self.ground_sprite = pygame.image.load("assets/sprites/Ground.png").convert()
        self.wall_sprite = pygame.image.load("assets/sprites/Wall.png").convert()
        self.running = True 
        self.clock = pygame.time.Clock()
        self.player = Player(20,20,self.player_sprite,3)
        self.map = Map(self.res,self.wall_sprite,self.ground_sprite,self.scale)
        self.carte = self.map.make_maze()
        self.carte[1][1] = True


    def handle_inputs(self,player):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_LSHIFT] and not player.is_sprint:
            player.speed = player.speed*1.5
            player.is_sprint = True
        if not pressed[pygame.K_LSHIFT] and player.is_sprint:
            player.speed = player.speed/1.5
            player.is_sprint = False
        if pressed[pygame.K_z]:
            player.move_up()  
        if pressed[pygame.K_s]:
            player.move_down()  
        if pressed[pygame.K_q]:
            player.move_left() 
        if pressed[pygame.K_d]:
            player.move_right() 

    def draw_map(self,scale):
        wall_coll = []
        for i in range(20):
            for j in range(30):
                if not self.carte[i][j]:
                    wall_coll.append(pygame.Rect(j*scale,i*scale,scale,scale))
                    self.screen.blit(self.map.mur,(j*scale,i*scale))
                    #pygame.draw.rect(self.screen,self.map.mur,pygame.Rect(j*scale,i*scale,scale,scale))
                else:
                    self.screen.blit(self.map.sol,(j*scale,i*scale))
                    #pygame.draw.rect(self.screen,self.map.sol,pygame.Rect(j*scale,i*scale,scale,scale))
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
        self.screen.blit(self.player.sprite[self.player.orientation],(self.player.x,self.player.y))
        #pygame.draw.rect(self.screen,self.player.sprite[self.player.orientation],self.player.coll)

    def run(self):
        while self.running:
            self.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            pygame.display.flip()
            self.clock.tick(60)

