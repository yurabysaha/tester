# -*- coding: utf-8 -*-
import pygame
import sys


class Results:
    def __init__(self, player):
        current_result = player.bug_kill - (player.bug_miss * 2)
        # update_result(player.name, current_result)
        self.result = 'Yours salary: ' + str(player.bug_kill - (player.bug_miss*2)) + ' $'
        if player.bug_kill <= -1:
            self.result = 'Game over'
        self.punkti = [['Retest', (240, 270)], ['Quit', (250, 320)]]
        self.punkt = -1

    def render(self, screen):
        menu_font = pygame.font.Font(None, 50)
        screen.blit(menu_font.render(self.result, 1, (255, 154, 43)), (200, 200))
        for i in self.punkti:
            if self.punkti.index(i) == self.punkt:
                screen.blit(menu_font.render(i[0], 1, (255, 154, 43)), i[1])
            else:
                screen.blit(menu_font.render(i[0], 1, (200, 154, 43)), i[1])

    def results(self, window, player):
        done = True
        pygame.font.init()
        screen = pygame.Surface((600, 630))
        while done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        if len(self.punkti)-1 != self.punkt:
                            self.punkt +=1
                        else:
                            self.punkt = 0
                    if event.key == pygame.K_UP:
                        if len(self.punkti) - 1 != self.punkt:
                            self.punkt += 1
                        else:
                            self.punkt = 0
                    if event.key == pygame.K_RETURN:
                        if self.punkt == 0:
                            done = False
                        elif self.punkt == 1:
                            pygame.quit()
                            sys.exit()

            screen.fill((40, 110, 120))
            self.render(screen)
            window.blit(screen, (0, 0))

            pygame.display.flip()

