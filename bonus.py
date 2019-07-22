from pygame.sprite import Sprite, collide_rect
from pygame.image import load
from pygame.surface import Surface

SCREEN_COLOR = (80, 80, 80)


class Bonus(Sprite):
    def __init__(self, x=10, y=10, speed=3):
        Sprite.__init__(self)
        self.image = Surface((35, 35))
        self.image = load("images/bonus/time.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed

    def update(self, player, timer):
        if self.rect.y < 600:
            self.rect.y += self.speed
            self.collision(player, timer)
        else:
            self.kill()

    def collision(self, player, timer):
        if collide_rect(self, player):
            self.kill()
            timer.start += 5

