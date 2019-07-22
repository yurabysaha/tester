import pygame
import sys


class Records:
    def __init__(self):
        self.punkti = [['User1 = 450 $', (250, 170)], ['User2 = 420 $', (250, 220)], ['User3 = 390 $', (250, 270)]]

    def render(self, screen):
        menu_font = pygame.font.Font(None, 50)
        for i in self.punkti:
            screen.blit(menu_font.render(i[0], 1, (255, 154, 43)), i[1])

    def record(self, window):
        done = True
        pygame.font.init()
        screen = pygame.Surface((800, 630))
        while done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                            done = False

            screen.fill((40, 110, 120))
            self.render(screen)
            window.blit(screen, (0, 0))

            pygame.display.flip()
