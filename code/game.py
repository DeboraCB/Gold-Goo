#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from code.menu import Menu


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(600, 480))
        self.player = None
        self.enemies = None
        self.coins = None
        self.map = None
        self.menu = None
        self.background = None
        self.start = None
        self.update = None
        self.handle_events = None
        self.switch_scene = None




    def run(self):
        while True:
            menu = Menu(self.window)
            menu.run()
            pass

            # # Check for all events
            # for event in pygame.event.get():
            #     if event.type == pygame.QUIT:
            #         pygame.quit()  # Close Window
            #         quit()  # end pygame