# -*- coding: utf-8 -*-
import random
import sys, pygame
import time

from menu import Menu
from player import Player
from bug import Bug
from results import Results

pygame.init()
''' Вікно '''
size = width, height = 800, 630
window = pygame.display.set_mode(size)
''' Скріни '''
info_screen = pygame.Surface((800, 30))
screen = pygame.Surface((800, 600))
'''Шрифти'''
pygame.font.init()
inf_font = pygame.font.Font(None, 32)
'''Меню'''
menu = Menu()
menu.menu(window)

player = Player()
left = right = False
sprite_group = pygame.sprite.Group()
sprite_group.add(player)
bug_army = []
timer_init = time.time() + 30


def timer():
    return timer_init - time.time()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                left = True
            if event.key == pygame.K_RIGHT:
                right = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                left = False
            if event.key == pygame.K_RIGHT:
                right = False
            if event.key == pygame.K_ESCAPE:
                menu.menu(window)

    '''Заливка'''
    screen.fill((80, 80, 80))
    info_screen.fill((50, 50, 50))

    player.move(left, right)
    # Створюємо баги
    if len(bug_army) < 4:
        while len(bug_army) != 4:
            rand = random.randrange(10, 750)
            rand_speed = random.randrange(1, 5)
            bug = Bug(x=rand, speed=rand_speed)
            bug_army.append(bug)
            sprite_group.add(bug)
    sprite_group.draw(screen)

    for b in bug_army:
        b.move(player, bug_army)

    info_screen.blit(inf_font.render(u'Багов закрыто: '+str(player.bug_kill), 1, (212, 120, 49)),(10,5))
    info_screen.blit(inf_font.render(u'Время до релиза: ' + str(int(timer())), 1, (212, 120, 49)), (250, 5))
    info_screen.blit(inf_font.render(u'Багов в релизе: ' + str(player.bug_miss), 1, (212, 120, 49)), (550, 5))
    if timer() < 0:
        Results(player.bug_kill).results(window)
    window.blit(info_screen, (0, 0))
    window.blit(screen, (0, 30))

    pygame.display.flip()