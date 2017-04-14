# -*- coding: utf-8 -*-
from pygame.sprite import Sprite, collide_rect
import pyganim
from pygame.image import load

SCREEN_COLOR = (180, 180, 180, 0)

MOVE_ANIMATION = [("images/bug/bug.png", 110), ("images/bug/bug1.png", 110), ("images/bug/bug2.png", 110)]


class Bug(Sprite):
    def __init__(self, x=10, y=10, speed=3):
        Sprite.__init__(self)
        self.image = load('images/bug/bug.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
        self.animation = pyganim.PygAnimation(MOVE_ANIMATION)
        self.animation.convert_alpha()
        self.animation.play()

    def move(self, player, bug_army, suriken_move):
        if self.rect.y < 600:
            self.rect.y += self.speed
            self.collision(player, bug_army, suriken_move)
            self.image.fill(SCREEN_COLOR)
            self.animation.blit(self.image, (0, 0))

        else:
            self.remove(bug_army)
            player.bug_miss += 1

    def collision(self, player, bug_army, suriken_move):
        if collide_rect(self, player):
            self.remove(bug_army)
            player.bug_kill +=1
        for z in bug_army:
            if collide_rect(self, z):
                self.rect.x -= 20
                z.rect.x += 20
        for i in suriken_move:
            if collide_rect(self, i):
                self.remove(bug_army)
                i.remove(suriken_move)
                player.bug_kill += 1

    def remove(self, bug_army):
        self.kill()
        try:
            bug_army.remove(self)
        except ValueError:
            pass
