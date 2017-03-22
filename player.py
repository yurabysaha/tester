# -*- coding: utf-8 -*-
from pygame.image import load
from pygame.sprite import Sprite

MOVE_SPEED = 3


class Player(Sprite):
    def __init__(self, x=10, y=535):
        Sprite.__init__(self)
        self.image = load("player.png")

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.bug_kill = 0
        self.bug_miss = 0

    def move(self, left, right):
       if left:
           if self.rect.x > 8:
               self.rect.x += -MOVE_SPEED
       if right:
           if self.rect.x < 753:
               self.rect.x += MOVE_SPEED