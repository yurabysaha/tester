from pygame.sprite import Sprite, collide_rect
from pygame.image import load


class Bomb(Sprite):
    def __init__(self, x=10, y=10, speed=3):
        Sprite.__init__(self)
        self.image = load("images/feature/feature.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed

    def update(self, player, bomb_group, screen):
        if self.rect.y < 600:
            self.rect.y += self.speed
            self.collision(player, bomb_group, screen)
        else:
            self.kill()

    def collision(self, player, bomb_group, screen):

        # If bomb collide with player we remove -2 from player`s killed bugs
        if collide_rect(self, player):
            screen.fill((115, 43, 23))
            self.kill()
            player.bug_kill -= 2
            return

        # If bomb collide between we resolve it.
        for z in bomb_group:
            if collide_rect(self, z):
                self.rect.x -= 20
                z.rect.x += 20
