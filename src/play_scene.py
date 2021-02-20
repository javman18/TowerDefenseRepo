import pygame
from Scene import Scene
import random

class PlayScene (Scene):
    def __init__(self, app):
        self.app = app
        self.screen = app.screen
        super().__init__('PlayScene')
        
        
        
    def start(self):
        
        print('se inicia: ', self.name)
    
    
    def process_events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                self.app.change_scene('intro')
                print('se presiono una tecla')
            elif event.key == pygame.K_LEFT:
                pass
            elif event.key == pygame.K_RIGHT:
                pass
            elif event.key == pygame.K_SPACE:
                pass
                
            elif event.key == pygame.K_q:
                pass

            elif event.key == pygame.K_l:
                pass
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                pass
            elif event.key == pygame.K_RIGHT:
                pass
            
    
    def update(self):
        pass

    
    def draw(self):
        self.screen.fill((255,255,255))
        pygame.draw.rect(self.screen, (0, 255, 0), (0,750,self.app.width,50))

        pygame.display.update()
        

    
    def exit(self):
        print('termina: ', self.name)

    
        
