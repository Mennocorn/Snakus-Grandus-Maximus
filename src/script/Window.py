import pygame, time
from pygame.locals import *
import keyboard

import datetime


class Frame():
    display_size_x = 500
    display_size_y = 500
    display_size_unit = 25

    pygame.init()
    screen = pygame.display.set_mode((display_size_x, display_size_y))
    pygame.display.set_caption('Cooles Game, pre pre pre alpha -1')
    pygame.mouse.set_visible(False)

    BLUE = (0, 0, 255)
    now_time = datetime.datetime.now()
    screen.fill(BLUE)
    pygame.draw.rect(screen, BLUE, (200, 150, 100, 50))


a = Frame()