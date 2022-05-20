#IMPORT
import pygame
from player import Player
from map import Map
from random import randrange
from monster import Monster
from time import sleep

#CLASS
class Game:
    """
    CLASS GAME

    Cet objet est le coeur du jeu.
    C'est ici qu'est défini toutes les textures, 
    le joueur, le monstre, la fenêtre du jeu et 
    le boucle du jeu
    la boucle du jeu se fait ainsi :
        - met à jour le timer
        - met à jour la position du joueur
        - met aussi à jour la file du monstre
        - vérifie si la joueur n'est pas au bout du labyrinthe
        - vérifie si le joueur n'est pas dans un mur et si c'est le 
          cas le remettre à sa place d'avant
        - affiche les murs, le sol, le joueur, le monstre et le timer 
    """
    def __init__(self, scale):
        #multiplicateur sur le jeu
        self.scale = scale
        #taille de la fenêtre
        self.screen = pygame.display.set_mode()     
        x, y = self.screen.get_size()
        x -= 40
        y -= 40
        self.res = [int(x/40)*40,int(y/40)*40]
        if (self.res[0]//self.scale)%2 == 0:
            self.res[0] -= self.scale
        if (self.res[1]//self.scale)%2 == 0:
            self.res[1] -= self.scale   
        #écran pygame
        self.screen = pygame.display.set_mode(self.res)
        #musique du jeu
        self.music = 'assets/sounds/music.mp3'
        self.ear = 'assets/sounds/ear.mp3'
        pygame.init()
        pygame.font.init()
        pygame.mixer.init()
        pygame.mixer.music.load(self.music)
        
        #sprite du joueur
        self.player_sprite = [pygame.image.load("assets/sprites/Up_Carac.png").convert_alpha(),
                              pygame.image.load("assets/sprites/Down_Carac.png").convert_alpha(),
                              pygame.image.load("assets/sprites/Left_Carac.png").convert_alpha(),
                              pygame.image.load("assets/sprites/Right_Carac.png").convert_alpha()]
        #sprite du monstre
        self.monstre_sprite = [pygame.image.load("assets/sprites/Monster_Up.png").convert_alpha(),
                              pygame.image.load("assets/sprites/Monster_Down.png").convert_alpha(),
                              pygame.image.load("assets/sprites/Monster_Left.png").convert_alpha(),
                              pygame.image.load("assets/sprites/Monster_Right.png").convert_alpha()]
        #sprite du sol
        self.ground_sprite = pygame.image.load("assets/sprites/Ground.png").convert()
        #sprite du tp
        self.ground_tp_sprite = pygame.image.load("assets/sprites/Ground_tp.png").convert()
        #sprite des murs
        self.wall_sprite = pygame.image.load("assets/sprites/Wall.png").convert()
        #screamer
        self.screamer_sprite = pygame.transform.scale(pygame.image.load("assets/sprites/screamer.jpg").convert(),(self.res[0], self.res[1]))
        
        #booleen pour lancer la fenêtre et mettre le jeu en pause ou non
        self.running = True 
        self.playing = True
        self.screamer = False
        #clock du jeu
        self.clock = pygame.time.Clock()
        #joueur, map, et labyrinthe 
        self.player = Player(40,40,self.player_sprite,3)
        self.map = Map(self.res,self.wall_sprite,self.ground_sprite,(0,0))
        self.maze = self.map.maze
        self.map.tp = self.map.map.ground[-1]
        self.tp = pygame.Rect(self.map.tp[1]*self.scale,self.map.tp[0]*self.scale,40,40)
        self.monster = Monster(40,40,3,self.monstre_sprite,2,self.scale)
        #timer + nombre de frame
        self.timer = 0
        self.actual_frame = 0
        self.screamer_cooldown = 120
        #police pour le timer et l'écran de fin
        self.police = pygame.font.SysFont("monospace" ,60)
        self.police2 = pygame.font.SysFont("monospace" ,20)

        

        

    def handle_inputs(self,player):
        #récupère les touches pressées par le joueur et déplace le joueur
        pressed = pygame.key.get_pressed()
        if self.playing:
            if pressed[pygame.K_LSHIFT] and not player.is_sprint:
                player.speed = player.speed*2
                player.is_sprint = True
            if not pressed[pygame.K_LSHIFT] and player.is_sprint:
                player.speed = player.speed//2
                player.is_sprint = False
            if pressed[pygame.K_z]:
                player.move_up()  
            if pressed[pygame.K_s]:
                player.move_down()  
            if pressed[pygame.K_q]:
                player.move_left() 
            if pressed[pygame.K_d]:
                player.move_right() 
        if not self.playing:
            if pressed[pygame.K_RETURN]:
                self.running = False


    def draw_map(self):
        #dessine le labyrinthe et renvoie le collisions de tous les murs
        wall_coll = []
        for i in range(self.res[1]//self.scale):
            for j in range(self.res[0]//self.scale):
                if not self.maze[i][j]:
                    wall_coll.append(pygame.Rect(j*self.scale,i*self.scale,self.scale,self.scale))
                    self.screen.blit(self.map.mur,(j*self.scale,i*self.scale))
                else:
                    if (i,j) == self.map.tp:
                        self.screen.blit(self.ground_tp_sprite,(j*self.scale,i*self.scale))
                    else:
                        self.screen.blit(self.map.sol,(j*self.scale,i*self.scale))
        return wall_coll

    def check_coll(self,col):
        #vérifie si le joueur n'est pas dans un mur
        for collision in col:
            if self.player.coll.colliderect(collision):
                return True
        return False

    def check_coll_monster(self):
        #vérifie si le joueur est touché par le monstre
        if self.player.coll.colliderect(self.monster.coll):
            return True
        else:
            return False

    def update(self):
        #met à jour le jeu à chauqe frame
        #update du timer
        if self.playing:
            self.actual_frame += 1
            if self.actual_frame == 60:
                self.timer += 1
                self.actual_frame = 0
        if self.screamer:
            self.screamer_cooldown -= 1
        #efface ce qu'il y a sur l'écran
        self.screen.fill((0,0,0))
        #liste des collisions
        coll_list = self.draw_map()
        #sauvegarde des coordonées du joueur
        x,y = self.player.x,self.player.y
        #déplacement du joueur
        self.handle_inputs(self.player)
        #met à jour le joueur + modifie la file du monstre
        self.player.update_player()
        self.monster.new_location((self.player.x+20)//self.scale,(self.player.y+20)//self.scale)
        
        if self.screamer:
            self.screen.blit(self.screamer_sprite,(0,0))
            if self.screamer_cooldown <= 0:
                self.running = False
        #affiche écran de victoire si le joueur a fini le labyrinthe
        if self.player.coll.colliderect(self.tp):
            self.playing = False
            pygame.mixer.music.stop()
            pygame.draw.rect(self.screen,(255,255,255),pygame.Rect(self.res[0]//4,self.res[1]//4,2*self.res[0]//4,2*self.res[1]//4))
            self.screen.blit(self.police.render ("Congrats !", 1 , (255,0,0) ), (self.res[0]//4+155,self.res[1]//4+30))
            self.screen.blit(self.police.render ("Time : "+str(self.timer), 1 , (0,0,0) ), (self.res[0]//4+155,self.res[1]//4+140))
            self.screen.blit(self.police2.render ("Press ENTER to continue", 1 , (0,0,0) ), (self.res[0]//4+155,self.res[1]//4+240))
        #affiche game over si le joueur est touché par le monstre
        if self.check_coll_monster() and not self.screamer:
            pygame.mixer.music.stop()
            pygame.mixer.music.load(self.ear)
            pygame.mixer.music.play()
            self.playing = False
            self.screamer = True
        #replace le joueur si il est dans un mur
        if self.check_coll(coll_list):
            self.player.x = x
            self.player.y = y
        self.player.update_player() 
        #affiche le timer, le joueur et le monstre
        if self.playing:
            pygame.draw.rect(self.screen,(255,255,255),pygame.Rect(0,0,110,30))
            self.screen.blit(self.player.sprite[self.player.orientation],(self.player.x,self.player.y))
            if self.timer >= self.monster.start:
                self.monster.coll = pygame.Rect(40,40,40,40)
                self.monster.check_pos()
                self.monster.update_monster()
                self.screen.blit(self.monster.sprite[self.monster.orientation],(self.monster.x,self.monster.y))           
            self.screen.blit(self.police2.render ("Time :"+str(self.timer), 1 , (0,0,0) ), (5,5))

    def run(self):
        #boucle du jeu
        pygame.mixer.music.play(-1)
        while self.running:
            self.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            pygame.display.flip()
            self.clock.tick(60)

