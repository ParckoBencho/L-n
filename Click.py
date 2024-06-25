import pygame as pg
import Data
from Data import felter 
def click(window,font):
    pos = pg.mouse.get_pos()
    
    if(710 <= pos[0] <= 790 and Data.Page != 0):
        if(450 <= pos[1] <= 490):
            Data.Page -= 1
        
    elif(810 <= pos[0] <= 890 and Data.Page != 4):
        if(450 <= pos[1] <= 490):
            Data.Page += 1
    
    if(500 <= pos[0] <= 600 and 450 <= pos[1] <= 500):
        input_string = ""
        while True:
            for event in pg.event.get():
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_RETURN:
                        try:
                            Data.skat = int(input_string)
                        except ValueError:
                            pass
                        input_string = ""
                        return
                    elif event.key == pg.K_BACKSPACE:
                        input_string = input_string[:-1]
                    else:
                        input_string += event.unicode
                        pg.draw.rect(window,"black",pg.Rect(500,450,100,50))
                        pg.draw.rect(window,"White",pg.Rect(500,450,100,50),2)
                        text = font.render(input_string + " %", True, (255,255,255))
                        textRect = text.get_rect()
                        textRect.center = (550,475)
                        window.blit(text, textRect)
                        pg.display.flip()

    
    else:
        for I in range(len(felter)):
            if(felter[I].x <= pos[0] <= felter[I].x+100):
                if(felter[I].y <= pos[1] <= felter[I].y+100):
                    if(felter[I].x == 200 and felter[I].y == 400 and Data.måneder[Data.Page] == 0):
                        break
                    else:
                        if(felter[I].dobbelt[Data.Page] == 1):
                            if(felter[I].y <= pos[1] < felter[I].y+50):
                                if(felter[I].valgt[Data.Page] == "morgen"):
                                    felter[I].valgt[Data.Page] = 0
                                else:
                                    felter[I].valgt[Data.Page] = "morgen"
                            elif(felter[I].y+50 <= pos[1] <= felter[I].y+100):
                                if(felter[I].valgt[Data.Page] == "aften"):
                                    felter[I].valgt[Data.Page] = 0
                                else:
                                    felter[I].valgt[Data.Page] = "aften"
                        else:
                            if(felter[I].valgt[Data.Page] == True):
                                    felter[I].valgt[Data.Page] = 0
                            else:
                                felter[I].valgt[Data.Page] = True


