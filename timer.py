# -*- coding: utf-8 -*-
import time

DEFAULT_TIME = 30


class Timer(object):
    def __init__(self):
        self.start = 0
        self.paused = 0
        self.start_game()

    def start_game(self):
        self.start = time.time() + DEFAULT_TIME

    def pause_game(self):
        self.paused = time.time()

    def unpause_game(self):
        self.start += time.time() - self.paused

    def lost_time(self):
        return self.start - time.time()
