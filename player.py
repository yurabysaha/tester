# -*- coding: utf-8 -*-
import pyganim
from pygame.image import load
from pygame.sprite import Sprite

MOVE_SPEED = 7
SCREEN_COLOR = (80, 80, 80, 0)

MOVE_ANIMATION = [("images/player/player.png", 100), ("images/player/player-f1.png", 100), ("images/player/player-f2.png", 100)]


class Player(Sprite):
    def __init__(self, x=10, y=535):
        Sprite.__init__(self)
        self.image = load("images/player/player.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.name = ''
        self.rect.x = x
        self.rect.y = y
        self.bug_kill = 0
        self.bug_miss = 0
        self.animation = pyganim.PygAnimation(MOVE_ANIMATION)
        self.animation.play()

    def move(self, left, right):
        if left:
            if self.rect.x > 8:
                self.rect.x += -MOVE_SPEED

        if right:
            if self.rect.x < 553:
                self.rect.x += MOVE_SPEED

        if right or left:
            self.image.fill(SCREEN_COLOR)
            self.animation.blit(self.image, (0, 0))

    def refresh(self):
        self.rect.x = 10
        self.rect.y = 535
        self.bug_kill = 0
        self.bug_miss = 0
