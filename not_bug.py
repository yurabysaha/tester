# -*- coding: utf-8 -*-
from pygame import Surface
from pygame.sprite import Sprite, collide_rect
from pygame.image import load


class NotBug(Sprite):
    def __init__(self, x=10, y=10, speed=3):
        Sprite.__init__(self)
        self.image = load("images/feature/feature.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed

    def move(self, player, bug_police):
        if self.rect.y < 600:
            self.rect.y += self.speed
            self.collision(player, bug_police)
        else:
            self.remove(bug_police)

    def collision(self, player, bug_police):
        if collide_rect(self, player):
            self.remove(bug_police)
            player.bug_kill -= 2

    def remove(self, bug_police):
        self.kill()
        bug_police.remove(self)
