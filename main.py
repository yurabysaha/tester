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
menu.menu(window)

player = Player()
player.name = "".join(menu.current_login)
left = right = False
sprite_group = pygame.sprite.Group()
sprite_group.add(player)

bug_army = []
bug_police = []
bonus_array = []
timer = Timer()
suriken_move = []
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
                if not suriken_move:
                    suriken = Suriken(x=player.rect.x, y=player.rect.y)
                    suriken_move.append(suriken)
                    sprite_group.add(suriken)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                left = False
            if event.key == pygame.K_RIGHT:
                right = False

            if event.key == pygame.K_ESCAPE:
                timer.pause_game()
                menu.menu(window)
                timer.unpause_game()

    '''Заливка'''
    screen.blit(bg_image, (0, 0))
    info_screen.fill((50, 50, 50))

    # Create bugs
    if len(bug_army) < 4:
        while len(bug_army) != 4:
            rand = random.randrange(10, 550)
            rand_speed = random.randrange(1, 5)
            bug = Bug(x=rand, speed=rand_speed)
            bug_army.append(bug)
            sprite_group.add(bug)

    # Create bombs
    if len(bug_police) < 2:
        while len(bug_police) != 2:
            rand = random.randrange(10, 550)
            rand_speed = random.randrange(1, 5)
            notbug = Bomb(x=rand, speed=rand_speed)
            bug_police.append(notbug)
            sprite_group.add(notbug)

    if not bonus_array and int(timer.lost_time()) % 10 == 0:
            rand = random.randrange(10, 550)
            rand_speed = random.randrange(10, 11)
            bonus = Bonus(x=rand, speed=rand_speed)
            bonus_array.append(bonus)
            sprite_group.add(bonus)
    sprite_group.draw(screen)

    # All moves here)
    player.move(left, right)
    for b in bug_army:
        b.move(player, bug_army, suriken_move)
    for b in bug_police:
        b.move(player, bug_police, screen)
    for i in suriken_move:
        i.move(suriken_move)
    for i in bonus_array:
        i.move(player, bonus_array, timer)

    info_screen.blit(inf_font.render('Bags closed: '+str(player.bug_kill), 1, (212, 120, 49)), (10,5))
    info_screen.blit(inf_font.render('Time to release: ' + str(int(timer.lost_time())), 1, (212, 120, 49)), (190, 5))
    info_screen.blit(inf_font.render('Bags in release: ' + str(player.bug_miss), 1, (212, 120, 49)), (400, 5))

    if timer.lost_time() < 0 or player.bug_kill <= -1:
        # Після натискання Ретест обнуляємо всі елементи в грі
        res = Results(player)
        res.results(window, player)
        player.refresh()
        timer.start_game()
        for i in bug_army:
            i.remove(bug_army)
        for i in bug_police:
            i.remove(bug_police)

    window.blit(info_screen, (0, 0))
    window.blit(screen, (0, 30))

    pygame.display.flip()
    fps.tick(60)
