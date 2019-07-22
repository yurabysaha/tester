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

    def update(self, player, bugs_group, suriken_group):
        if self.rect.y < 600:
            self.rect.y += self.speed
            self.collision(player, bugs_group, suriken_group)
            self.image.fill(SCREEN_COLOR)
            self.animation.blit(self.image, (0, 0))

        else:
            self.remove(bugs_group)
            player.bug_miss += 1

    def collision(self, player, bugs_group, surikens_group):

        # If bug collide with player.
        if collide_rect(self, player):
            self.kill()
            player.bug_kill += 1

        # If bugs collide between self we resolve it
        for z in bugs_group:
            if collide_rect(self, z):
                self.rect.x -= 20
                z.rect.x += 20

        # Check collision with any suriken
        for i in surikens_group:
            if collide_rect(self, i):
                self.kill()
                i.remove(surikens_group)
                player.bug_kill += 1
