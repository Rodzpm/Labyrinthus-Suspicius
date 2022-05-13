import pygame

class Game:
    def __init__(self, res):
        self.res = res
        self.screen = pygame.display.set_mode(res)
        self.running = True 
        self.clock = pygame.time.Clock()

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            pygame.display.flip()
            self.clock.tick(60)

