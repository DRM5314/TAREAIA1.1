import math
import time
class Robot():
    nombre = "RBC1"
    posX = 0
    posY = 0
    sizeX = 10
    sizeY = 15

    def __init__(self, nombre):
        self.nombre = nombre

    def move(self,posX,posY):
        self.posX = posX
        self.posY = posY
        time.sleep(.4)

    def clean(self):
        print("limpio")
        time.sleep(2)
        return "-"

    def scan (self,condition):
        if(condition == "d"):
            self.clean()
            return "d~"
        else:
            return condition

    def cleanRadio(self,radio,angle):
        for i in range(radio):
            self.posX = math.cos(angle) * radio
            self.posY = math.sin(angle) * radio
            print("Cleaning!! Area Clean: x= " + self.posX + " y= " + self.posY)
            time.sleep(.07)

    def wichMyPosition(self):
        print("My position is x: "+self.posX+" y: "+self.posY)

    def getPosX(self):
        return self.posX

    def getPosY(self):
        return self.posY