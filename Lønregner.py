import pygame as pg
import sys
from Redraw import redraw
from Felter import initialize
from Click import click
from Udregner import Udregner


pg.init()

size = 900,500

window = pg.display.set_mode(size)
font = pg.font.SysFont('arial', 15)


def Main(window):
    run = True 
    initialize()
    pg.display.set_caption("Løn Regner")

    LønHøj = 0
    LønLav = 0

    while run:
        for event in pg.event.get():
            if(event.type == pg.QUIT):
                run = False
                sys.exit()
            elif(event.type == pg.MOUSEBUTTONUP):
                click(window,font)

        HøjLøn,LavLøn = Udregner(LønHøj,LønLav)
        redraw(window,font,HøjLøn,LavLøn)

Main(window)