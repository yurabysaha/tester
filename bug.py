# -*- coding: utf-8 -*-
from pygame import Surface
from pygame.sprite import Sprite, collide_rect
from pygame.image import load


class Bug(Sprite):
    def __init__(self, x=10, y=10, speed=3):
        Sprite.__init__(self)
        self.image = load("images/bug.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed

    def move(self, player, bug_army):
        if self.rect.y < 600:
            self.rect.y += self.speed
            self.collision(player, bug_army)
        else:
            bug_army.remove(self)
            player.bug_miss += 1

    def collision(self, player, bug_army):
        if collide_rect(self, player):
            self.kill()
            bug_army.remove(self)
            player.bug_kill +=1
