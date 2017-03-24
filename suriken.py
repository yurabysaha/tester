# -*- coding: utf-8 -*-
from pygame.image import load
from pygame.sprite import Sprite

MOVE_SPEED = 7


class Suriken(Sprite):
    def __init__(self, x=10, y=535):
        Sprite.__init__(self)
        self.image = load("images/suriken.png")

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def move(self, suriken_move):
        if self.rect.y >= 0:
            self.rect.y += -MOVE_SPEED
        else:
            self.kill()
            suriken_move.remove(self)