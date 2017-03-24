# -*- coding: utf-8 -*-
import time
from pygame.image import load
from pygame.sprite import Sprite

DEFAULT = 30

class Timer(object):

    def __init__(self):
        self.start = 0
        self.paused = 0
        self.unpaused = 0
        self.start_game()

    def start_game(self):
        self.start = time.time() + DEFAULT

    def pause_game(self):
        self.paused = time.time()

    def unpause_game(self):
        self.unpaused = time.time()
        t = self.unpaused - self.paused
        self.start += t

    def lost_time(self):
        return self.start - time.time()


