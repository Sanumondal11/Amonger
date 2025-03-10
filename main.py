import os
import random
import math
import pygame as pg
from os import listdir
from os.path import isfile, join

pg.init()
# this is just a test
pg.display.set_caption("Amonger")

BG_COLOR = (255,255,255)
WIDTH,HEIGHT = 1000,800
FPS=60
PLAYER_VEL=3

window = pg.display.set_mode((WIDTH,HEIGHT))

def main(window):
    clock = pg.time.Clock()

    run=True
    while run:
        clock.tick(FPS)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                run=False
                break
    pg.quit()
    quit()

if __name__ == '__main__':
    main(window)