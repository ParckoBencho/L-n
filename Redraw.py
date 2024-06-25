import pygame as pg
import Data
from math import floor

def redraw(window,font,HøjLøn,LavLøn):
    window.fill("black")

    dage = 0
    for I in range(5):
        for II in range(7):
            if(dage-30 == Data.måneder[Data.Page]):
                break
            else:
                if(Data.felter[dage].valgt[Data.Page] == "morgen"):
                    pg.draw.rect(window,"Dark Green",pg.Rect(100*II,100*I,100,50))
                elif(Data.felter[dage].valgt[Data.Page] == "aften"):
                    pg.draw.rect(window,"Dark Green",pg.Rect(100*II,100*I+50,100,50))
                elif(Data.felter[dage].valgt[Data.Page] == True):
                    pg.draw.rect(window,"Dark Green",pg.Rect(100*II,100*I,100,100))


                pg.draw.rect(window,"white",pg.Rect(100*II,100*I,100,100),2)
                if(Data.flervagt[Data.Page] == 1):
                    pg.draw.line(window,"white",(100*II,50+100*I),(100*(II+1),50+100*I),2)
                elif(Data.felter[dage].dag[Data.Page] == 6 or Data.felter[dage].dag[Data.Page] == 7):
                    pg.draw.line(window,"white",(100*II,50+100*I),(100*(II+1),50+100*I),2)

                



                text = font.render(str(dage+1), True, (255,255,255))
                textRect = text.get_rect()
                textRect.center = (100*II+10,100*I+10)
                window.blit(text, textRect)
                

                dage += 1

    pg.draw.rect(window,"Dark Grey",pg.Rect(700,0,200,600))

    if(Data.Page != 0):
        pg.draw.rect(window,"Grey",pg.Rect(710,450,80,40))
        pg.draw.rect(window,"black",pg.Rect(710,450,80,40),2)
        text = font.render("Back", True, (0,0,0))
        textRect = text.get_rect()
        textRect.center = (750,470)
        window.blit(text, textRect)

    if(Data.Page != 4):
        pg.draw.rect(window,"Grey",pg.Rect(810,450,80,40))
        pg.draw.rect(window,"black",pg.Rect(810,450,80,40),2)
        text = font.render("Next", True, (0,0,0))
        textRect = text.get_rect()
        textRect.center = (850,470)
        window.blit(text, textRect)
    
    pg.draw.rect(window,"White",pg.Rect(600,450,100,50),2)
    text = font.render(Data.MånedNavne[Data.Page], True, (255,255,255))
    textRect = text.get_rect()
    textRect.center = (650,475)
    window.blit(text, textRect)

    pg.draw.rect(window,"White",pg.Rect(500,450,100,50),2)
    text = font.render(str(Data.skat) + " %", True, (255,255,255))
    textRect = text.get_rect()
    textRect.center = (550,475)
    window.blit(text, textRect)

    text = font.render("Skat", True, (255,255,255))
    textRect = text.get_rect()
    textRect.center = (550,440)
    window.blit(text, textRect)


    pg.draw.rect(window,"white",pg.Rect(720,50,160,80))
    pg.draw.rect(window,"black",pg.Rect(720,50,160,80),2)
    text = font.render(str(floor(HøjLøn)) + " DKK", True, (0,0,0))
    textRect = text.get_rect()
    textRect.center = (800,90)
    window.blit(text, textRect)
    text = font.render("Fuldtid", True, (0,0,0))
    textRect = text.get_rect()
    textRect.center = (800,40)
    window.blit(text, textRect)


    pg.draw.rect(window,"white",pg.Rect(720,180,160,80))
    pg.draw.rect(window,"black",pg.Rect(720,180,160,80),2)
    text = font.render(str(floor(LavLøn)) + " DKK", True, (0,0,0))
    textRect = text.get_rect()
    textRect.center = (800,220)
    window.blit(text, textRect)
    text = font.render("-1 time", True, (0,0,0))
    textRect = text.get_rect()
    textRect.center = (800,170)
    window.blit(text, textRect)


    pg.draw.rect(window,"white",pg.Rect(720,310,160,80))
    pg.draw.rect(window,"black",pg.Rect(720,310,160,80),2)
    pg.draw.line(window,"black",(799,310),(799,390),2)

    text = font.render(str(floor((HøjLøn*0.92)*(1-(Data.skat/100)))) + " DKK", True, (0,0,0))
    textRect = text.get_rect()
    textRect.center = (760,330)
    window.blit(text, textRect)

    text = font.render(str(floor((LavLøn*0.92)*(1-(Data.skat/100)))) + " DKK", True, (0,0,0))
    textRect = text.get_rect()
    textRect.center = (760,370)
    window.blit(text, textRect)

    text = font.render(str(floor(HøjLøn*0.92)) + " DKK", True, (0,0,0))
    textRect = text.get_rect()
    textRect.center = (840,330)
    window.blit(text, textRect)

    text = font.render(str(floor(LavLøn*0.92)) + " DKK", True, (0,0,0))
    textRect = text.get_rect()
    textRect.center = (840,370)
    window.blit(text, textRect)

    text = font.render("Skat + AMB", True, (0,0,0))
    textRect = text.get_rect()
    textRect.center = (760,300)
    window.blit(text, textRect)

    text = font.render("AMB", True, (0,0,0))
    textRect = text.get_rect()
    textRect.center = (840,300)
    window.blit(text, textRect)




    pg.display.flip()
