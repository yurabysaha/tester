# -*- coding: utf-8 -*-
from pygame.sprite import Sprite
import pyganim
from pygame.surface import Surface

MOVE_SPEED = 7
SCREEN_COLOR = (80, 80, 80)

ANIMATION = [("images/suriken/suriken.png", 120), ("images/suriken/suriken1.png", 120)]


class Suriken(Sprite):
    def __init__(self, x=10, y=535):
        Sprite.__init__(self)
        self.image = Surface((40,40))
        self.image.fill(SCREEN_COLOR)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.animation = pyganim.PygAnimation(ANIMATION)
        self.animation.play()

    def move(self, suriken_move):
        if self.rect.y >= 0:
            self.image.fill(SCREEN_COLOR)
            self.animation.blit(self.image, (0,0))
            self.rect.y += -MOVE_SPEED
        else:
            self.kill()
            suriken_move.remove(self)

    def remove(self, suriken_move):
        self.kill()
        suriken_move.remove(self)