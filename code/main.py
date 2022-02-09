import pygame
import sys
from settings import *
# print (sys.path)
class Game: 
    def __init__():
        # general setup
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
        self.clock = pygame.time.Clock()
    
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            self.screen.fill('block')
            pygame.display.update()
            self.clock.tick(FPS)    
    
if __name__=='__main__':
    pass
    # game = Game()
    # game.run()
