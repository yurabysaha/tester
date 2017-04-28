# -*- coding: utf-8 -*-
import string

import pygame
import sys
from records import Records


class Menu:
    def __init__(self):
        self.punkti = [[u'Го тестить!', (200, 270)], [u'Рекорд', (220, 320)], [u'Уйти', (240, 370)]]
        self.punkt = 0
        self.current_login = []

    def render(self, screen):
        menu_font = pygame.font.Font(None, 50)
        for i in self.punkti:
            if self.punkti.index(i) == self.punkt:
                screen.blit(menu_font.render(i[0], 1, (255, 154, 43)), i[1])
            else:
                screen.blit(menu_font.render(i[0], 1, (200, 154, 43)), i[1])

    def menu(self, window):
        done = True
        pygame.font.init()
        screen = pygame.Surface((800, 630))

        login_font = pygame.font.Font(None, 35)
        while done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        if len(self.punkti)-1 != self.punkt:
                            self.punkt += 1
                        else:
                            self.punkt = 0
                    if event.key == pygame.K_UP:
                        if self.punkt != 0:
                            self.punkt -= 1
                        else:
                            self.punkt = len(self.punkti)-1
                    if event.key == pygame.K_RETURN:
                        if self.punkt == 0:
                            done = False
                        elif self.punkt == 1:
                            Records().record(window)
                        else:
                            sys.exit()

                    if event.key == pygame.K_BACKSPACE:
                        self.current_login = self.current_login[0:-1]
                    elif event.key == pygame.K_RETURN:
                        break
                    elif event.key <= 127:
                        self.current_login.append(chr(event.key))

            screen.fill((40, 110, 120))
            self.render(screen)
            pygame.draw.rect(screen, (0, 0, 0), (180, 100, 200, 30), 1)
            screen.blit(login_font.render('Enter login: ' + string.join(self.current_login, ""), 1, (255, 154, 43)), (40, 100))
            window.blit(screen, (0, 0))

            pygame.display.flip()
