# -*- coding: utf-8 -*-
from pygame import Surface
from pygame.sprite import Sprite, collide_rect
from pygame.image import load


class NotBug(Sprite):
    def __init__(self, x=10, y=10, speed=3):
        Sprite.__init__(self)
        self.image = load("images/hp.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
    #test
    def move(self, player, bug_police):
        if self.rect.y < 600:
            self.rect.y += self.speed
            self.collision(player, bug_police)
        else:
            bug_police.remove(self)

    def collision(self, player, bug_police):
        if collide_rect(self, player):
            self.kill()
            bug_police.remove(self)
            player.bug_kill -=1
