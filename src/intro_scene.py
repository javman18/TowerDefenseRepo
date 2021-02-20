from Scene import Scene
import pygame
import random

class IntroScene(Scene):
    def __init__(self, app):
        self.app = app
        self.screen = app.screen
        super().__init__('IntroScene') 
        
    def start(self):
        
        
        print('se inicia: ', self.name)
    
    
    def process_events(self, event):
        if event.type == pygame.KEYDOWN:
            self.app.change_scene('play')
            print('se presiono una tecla')

    def update(self):
        pass
        
    def draw(self):
        
        self.screen.fill((0,0,0))
        

    def exit(self):
        print('termina: ', self.name)

    
    