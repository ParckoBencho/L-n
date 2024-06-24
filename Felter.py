import Data

class felt():
    def __init__(self,x,y,valgt,dag,dobbelt):
        self.x = x
        self.y = y
        self.valgt = valgt
        self.dag = dag
        self.dobbelt = dobbelt

def initialize():
    dage = 0
    for I in range(5):
        for II in range(7):
            if(dage == 31):
                break
            else:
                ugedage = []
                for III in range(5):
                    if(dage+Data.startdag[III] > 7):
                        if((dage%7)+Data.startdag[III] > 7):
                            ugedage.append((dage%7)+Data.startdag[III]-7)
                        else:
                            ugedage.append((dage%7)+Data.startdag[III])
                    else:
                        ugedage.append(dage+Data.startdag[III])

                dobbel = []
                for III in range(5):
                    if(Data.flervagt[III] == 1):
                        dobbel.append(1)
                    elif(ugedage[III] == 6 or ugedage[III] == 7):
                        dobbel.append(1)
                    else:
                        dobbel.append(0)

                Data.felter.append(felt(100*II,100*I,[0,0,0,0,0],ugedage,dobbel))

                dage += 1


