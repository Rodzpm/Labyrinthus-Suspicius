import pygame
from player import Player
from map import Map
from random import randrange


class Game:
    def __init__(self, res, scale):
        self.res = res
        self.scale = scale
        self.screen = pygame.display.set_mode(res)
        pygame.font.init()
        self.player_sprite = [pygame.image.load("assets/sprites/Up_Carac.png").convert_alpha(),
                              pygame.image.load("assets/sprites/Down_Carac.png").convert_alpha(),
                              pygame.image.load("assets/sprites/Left_Carac.png").convert_alpha(),
                              pygame.image.load("assets/sprites/Right_Carac.png").convert_alpha()]
        self.ground_sprite = pygame.image.load("assets/sprites/Ground.png").convert()
        self.ground_tp_sprite = pygame.image.load("assets/sprites/Ground_tp.png").convert()
        self.wall_sprite = pygame.image.load("assets/sprites/Wall.png").convert()
        self.running = True 
        self.playing = True
        self.clock = pygame.time.Clock()
        self.player = Player(40,40,self.player_sprite,3)
        self.map = Map(self.res,self.wall_sprite,self.ground_sprite,(0,0))
        self.maze = self.map.maze
        self.map.tp = self.map.map.ground[-1]
        self.tp = pygame.Rect(self.map.tp[1]*self.scale,self.map.tp[0]*self.scale,40,40)
        self.timer = 0
        self.actual_frame = 0
        self.police = pygame.font.SysFont("monospace" ,60)
        self.police2 = pygame.font.SysFont("monospace" ,20)
        

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

    def draw_map(self):
        wall_coll = []
        for i in range(self.res[1]//self.scale):
            for j in range(self.res[0]//self.scale):
                if not self.maze[i][j]:
                    wall_coll.append(pygame.Rect(j*self.scale,i*self.scale,self.scale,self.scale))
                    self.screen.blit(self.map.mur,(j*self.scale,i*self.scale))
                    #pygame.draw.rect(self.screen,self.map.mur,pygame.Rect(j*scale,i*scale,scale,scale))
                else:
                    if (i,j) == self.map.tp:
                        self.screen.blit(self.ground_tp_sprite,(j*self.scale,i*self.scale))
                    else:
                        self.screen.blit(self.map.sol,(j*self.scale,i*self.scale))
                    #pygame.draw.rect(self.screen,self.map.sol,pygame.Rect(j*scale,i*scale,scale,scale))
        self.t = 0
        return wall_coll

    def check_coll(self,col):
        for collision in col:
            if self.player.coll.colliderect(collision):
                return True
        return False

    def update(self):
        if self.playing:
            self.actual_frame += 1
            if self.actual_frame == 60:
                self.timer += 1
                self.actual_frame = 0
        self.screen.fill((0,0,0))
        coll_list = self.draw_map()
        x,y = self.player.x,self.player.y
        if self.playing:
            self.handle_inputs(self.player)
        self.player.update_player()
        if self.player.coll.colliderect(self.tp):
            self.playing = False
            pygame.draw.rect(self.screen,(255,255,255),pygame.Rect(310,210,620,420))
            self.screen.blit(self.police.render ("Congrats !", 1 , (255,0,0) ), (465,240))
            self.screen.blit(self.police.render ("Time : "+str(self.timer), 1 , (0,0,0) ), (465,350))
        if self.check_coll(coll_list):
            self.player.x = x
            self.player.y = y
        self.player.update_player() 
        if self.playing:
            pygame.draw.rect(self.screen,(255,255,255),pygame.Rect(0,0,110,30))
            self.screen.blit(self.player.sprite[self.player.orientation],(self.player.x,self.player.y))
            self.screen.blit(self.police2.render ("Time :"+str(self.timer), 1 , (0,0,0) ), (5,5))
        #pygame.draw.rect(self.screen,self.player.sprite[self.player.orientation],self.player.coll)

    def run(self):
        while self.running:
            self.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            pygame.display.flip()
            self.clock.tick(60)

