import os
import random
import pygame as py
import math
from os import listdir
from os.path import isfile,join
py.init()

py.display.set_caption("Amonger")

WIDTH,HEIGHT=1000,800
FPS=60
PLAYER_VEL=3

window = py.display.set_mode((WIDTH,HEIGHT))

# background
def get_background(name):
    image = py.image.load(join("assests","Background",name))
    _,_,width,height=image.get_rect()
    tiles=[]
    for i in range(WIDTH//width+1):
        for j in range(HEIGHT//height+1):
            pos = [i*width,j*height]
            tiles.append(pos)
    return tiles,image

def draw(window,background,bg_image):
    for tile in background:
        window.blit(bg_image,tuple(tile)) 

    py.display.update()

def main(window):
    clock=py.time.Clock()
    background,bg_image=get_background("Green.png")
    run=True
    while run:
        clock.tick(FPS)

        for event in py.event.get():
            if event.type == py.QUIT:
                run = False
                break

        draw(window,background,bg_image)

    py.quit()
    quit()

if "__name__"=="__main__":
    main(window) 