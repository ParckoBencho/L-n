from Data import felter

def Udregner(LønHøj,LønLav):
    timeløn = 141.54
    AftenTillæg = 27.11
    LørdagMorgen = 32.19
    Søndag = 59.30

    for I in range(len(felter)):
        for II in range(5):
            if(felter[I].valgt[II] != 0):
                if(II <= 1):
                    if(felter[I].valgt[II] == True):
                        LønHøj += (timeløn*9)+(AftenTillæg*4.5)
                        LønLav += (timeløn*8)+(AftenTillæg*3.5)

                    if(felter[I].valgt[II] == "morgen"):
                        if(felter[I].dag[II] == 6):
                            LønHøj += (timeløn*8)+(LørdagMorgen*3.5)
                            LønLav += (timeløn*8)+(LørdagMorgen*3.5)
                        if(felter[I].dag[II] == 7):
                            LønHøj += (timeløn*8)+(Søndag*8)
                            LønLav += (timeløn*8)+(Søndag*8)

                    if(felter[I].valgt[II] == "aften"):
                        if(felter[I].dag[II] == 6):
                            LønHøj += (timeløn*7)+(LørdagMorgen*2.5)+(Søndag*4.5)
                            LønLav += (timeløn*6)+(LørdagMorgen*2.5)+(Søndag*3.5)
                        if(felter[I].dag[II] == 7):
                            LønHøj += (timeløn*7.5)+(Søndag*7.5)
                            LønLav += (timeløn*6.5)+(Søndag*6.5)

                else:
                    if(felter[I].valgt[II] == "morgen"):
                        if(felter[I].dag[II] == 6):
                            LønHøj += (timeløn*8)+(LørdagMorgen*3.5)
                            LønLav += (timeløn*8)+(LørdagMorgen*3.5)
                        elif(felter[I].dag[II] == 7):
                            LønHøj += (timeløn*8)+(Søndag*8)
                            LønLav += (timeløn*8)+(Søndag*8)
                        else:
                            LønHøj += (timeløn*6)
                            LønLav += (timeløn*6)

                    if(felter[I].valgt[II] == "aften"):
                        if(felter[I].dag[II] == 6):
                            LønHøj += (timeløn*7)+(LørdagMorgen*2.5)+(Søndag*4.5)
                            LønLav += (timeløn*6)+(LørdagMorgen*2.5)+(Søndag*3.5)
                        elif(felter[I].dag[II] == 7):
                            LønHøj += (timeløn*7.5)+(Søndag*7.5)
                            LønLav += (timeløn*6.5)+(Søndag*6.5)
                        else:
                            LønHøj += (timeløn*6)+(4.5*AftenTillæg)
                            LønLav += (timeløn*5)+(3.5*AftenTillæg)
    
    return LønHøj,LønLav
