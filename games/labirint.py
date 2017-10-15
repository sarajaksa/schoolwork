import pygame, sys
from pygame.locals import *
import random

class MapGame():

    def __init__(self):
    
        #colors used
        self.BLACK = (0,0,0)
        self.WHITE = (255,255,255)
        self.BLUE = (0,0,255)
        self.RED = (255,0,0)
        self.YELLOW = (200, 200, 0)
        #begining position
        self.position_y = 288
        self.position_x = 38
        #finish position
        self.finish_y = 388
        self.finish_x = 538
        #levels
        self.levels = [0.8]
        self.current_level = 0
        #pygame
        pygame.init()
        self.DISPLAYSURF = pygame.display.set_mode((800, 600))
        #create first level
        self.walls = self.create_level(self.levels[self.current_level])
        
        #game
        while True: 
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                    pygame.display.update()    
                elif event.type == KEYUP:
                    if event.key in (K_LEFT, K_a) and self.position_y > 25 and (self.position_y - 13 - 25, self.position_x - 13) not in self.walls:
                        self.position_y -= 25
                        self.already_won()
                    elif event.key in (K_RIGHT, K_d) and self.position_y < 775 and (self.position_y - 13 + 25, self.position_x - 13) not in self.walls:
                        self.position_y += 25
                        self.already_won()
                    elif event.key in (K_UP, K_w) and self.position_x > 25 and (self.position_y - 13 , self.position_x - 13 - 25) not in self.walls:
                        self.position_x -= 25
                        self.already_won()
                    elif event.key in (K_DOWN, K_s) and self.position_x < 575 and (self.position_y - 13, self.position_x - 13 + 25) not in self.walls:
                        self.position_x += 25
                        self.already_won()
    
            self.draw_all()   
            pygame.display.update()
    
    def already_won(self):
        if self.position_x == self.finish_x and self.position_y == self.finish_y:
            pygame.quit()
            sys.exit()
      
    def create_level(self, hard):
        i_elements = list(range(0,32))
        j_elements = list(range(0,24))
        walls = set()
        for i in i_elements:
            for j in j_elements:
                if random.random() > hard:
                    walls.add((i*25, j*25)) 
        return walls

    def draw_all(self):
        self.DISPLAYSURF.fill(self.WHITE)
            
        for i, j in self.walls:
            pygame.draw.rect(self.DISPLAYSURF, self.RED, (i, j, 25, 25))
                    
        for i in range(1,24):
            pygame.draw.line(self.DISPLAYSURF, self.BLACK, (0,i*25), (800, i*25), 1)
        for i in range(1,32):
            pygame.draw.line(self.DISPLAYSURF, self.BLACK, (i*25,0), (i*25, 600), 1)
            
        pygame.draw.circle(self.DISPLAYSURF, self.BLUE, (self.position_y, self.position_x), 12, 0)
        pygame.draw.circle(self.DISPLAYSURF, self.YELLOW, (self.finish_y, self.finish_x), 12, 0)


a = MapGame()    
