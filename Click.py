import pygame as pg
import Data
from Data import felter 
def click():
    pos = pg.mouse.get_pos()
    
    if(710 <= pos[0] <= 790 and Data.Page != 0):
        if(450 <= pos[1] <= 490):
            Data.Page -= 1
        
    elif(810 <= pos[0] <= 890 and Data.Page != 4):
        if(450 <= pos[1] <= 490):
            Data.Page += 1
    
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


