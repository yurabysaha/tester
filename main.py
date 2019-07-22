import random
import sys, pygame

from bonus import Bonus
from menu import Menu
from bomb import Bomb
from player import Player
from bug import Bug
from results import Results
from timer import Timer
from suriken import Suriken
from pygame.image import load

pygame.init()
pygame.mouse.set_visible(False)

''' Window '''
size = width, height = 600, 630
window = pygame.display.set_mode(size)

''' Screens '''
info_screen = pygame.Surface((600, 30))
screen = pygame.Surface((600, 600))
bg_image = load('images/bg.png')

'''Fonts'''
pygame.font.init()
inf_font = pygame.font.Font(None, 27)

'''Menu'''
menu = Menu()
menu.display_menu(window)

player = Player()
player.name = "".join(menu.current_login)
left = right = False
player_group = pygame.sprite.Group()
player_group.add(player)

bugs_group = pygame.sprite.Group()
bombs_group = pygame.sprite.Group()
bonuses_group = pygame.sprite.Group()
surikens_group = pygame.sprite.Group()

timer = Timer()

fps = pygame.time.Clock()


while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                left = True
            if event.key == pygame.K_RIGHT:
                right = True

            if event.key == pygame.K_SPACE:
                if not surikens_group:
                    suriken = Suriken(x=player.rect.x, y=player.rect.y)
                    surikens_group.add(suriken)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                left = False
            if event.key == pygame.K_RIGHT:
                right = False

            if event.key == pygame.K_ESCAPE:
                timer.pause_game()
                menu.display_menu(window)
                timer.unpause_game()

    '''Заливка'''
    screen.blit(bg_image, (0, 0))
    info_screen.fill((50, 50, 50))

    # Create bugs
    if len(bugs_group) < 4:
        while len(bugs_group) != 4:
            rand = random.randrange(10, 550)
            rand_speed = random.randrange(1, 5)
            bug = Bug(x=rand, speed=rand_speed)
            bugs_group.add(bug)

    # Create bombs
    if len(bombs_group) < 2:
        while len(bombs_group) != 2:
            rand = random.randrange(10, 550)
            rand_speed = random.randrange(1, 5)
            bomb = Bomb(x=rand, speed=rand_speed)
            bombs_group.add(bomb)

    if not bonuses_group and int(timer.lost_time()) % 10 == 0:
            rand = random.randrange(10, 550)
            rand_speed = random.randrange(10, 11)
            bonus = Bonus(x=rand, speed=rand_speed)
            bonuses_group.add(bonus)

    # Draw all elements
    player_group.draw(screen)
    bugs_group.draw(screen)
    bombs_group.draw(screen)
    bonuses_group.draw(screen)
    surikens_group.draw(screen)

    # All moves here)
    player_group.update(left, right)
    bugs_group.update(player, bugs_group, surikens_group)
    bombs_group.update(player, bombs_group, screen)
    bonuses_group.update(player, bonuses_group, timer)
    surikens_group.update(surikens_group)

    info_screen.blit(inf_font.render('Bags closed: '+str(player.bug_kill), 1, (212, 120, 49)), (10, 5))
    info_screen.blit(inf_font.render('Time to release: ' + str(int(timer.lost_time())), 1, (212, 120, 49)), (190, 5))
    info_screen.blit(inf_font.render('Bags in release: ' + str(player.bug_miss), 1, (212, 120, 49)), (400, 5))

    if timer.lost_time() < 0 or player.bug_kill <= -1:

        res = Results(player)
        res.results(window, player)
        # After click on Retest we empty all sprites
        player.refresh()
        bugs_group.empty()
        bombs_group.empty()
        timer.start_game()

    window.blit(info_screen, (0, 0))
    window.blit(screen, (0, 30))

    pygame.display.flip()
    fps.tick(60)
