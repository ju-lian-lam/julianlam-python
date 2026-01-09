from vpsettings import *
from os.path import join
from os import path

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load(join(path.dirname(__file__),"0.png")).convert_alpha()
        self.rect = self.image.get_frect(center = pos) 

    def input(self):
        pass

    def move(self, dt):
        self.rect.center += self.direction

    def update(self, dt):
        self.input()
        self.move(dt)