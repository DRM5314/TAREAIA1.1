import math
import time
class Robot():
    nombre = "RBC1"
    posX = 0
    posY = 0
    sizeX = 10
    sizeY = 15
    smart = True
    memory = "-"

    def __init__(self, nombre):
        self.nombre = nombre
        print("\nMi nombre es: "+self.nombre+", actualmente estoy configurado como: ")
        print("\n\tSmart: "+str(self.smart))
        print("\n\tTiempo limpieza: 4seg")
        print("\n\tTiempo para moverme entre cuadrantes: 2seg")
        print("\n\tTiempo de descanso: 10seg")
        time.sleep(10)

    def move(self,posX,posY):
        self.posX = posX
        self.posY = posY
        time.sleep(2)

    def clean(self):
        print("Limpiando.... *R*")
        time.sleep(4)
        print("limpio!")
        return "-"

    def scan (self,condition):
        if (condition == "-" or condition == "R"):
            print("Lugar limpio")
        elif (condition == "d"):
            print("Lugar sucio")

        if(self.smart):
            if (condition == "d"):
                return self.clean()
            else:
                return condition
        else:
            return self.clean()

    def cleanRadio(self,radio,angle):
        for i in range(radio):
            self.posX = math.cos(angle) * radio
            self.posY = math.sin(angle) * radio
            print("Cleaning!! Area Clean: x= " + self.posX + " y= " + self.posY)
            time.sleep(.07)

    def setSmart(self,bool):
        self.smart = bool

    def isSmart(self):
        return self.smart

    def setMemory(self,memory):
        if(memory!="R"):
            self.memory = memory

    def getMemory(self):
        return self.memory
    def wichMyPosition(self):
        print("My position is x: "+self.posX+" y: "+self.posY)

    def getPosX(self):
        return self.posX

    def getPosY(self):
        return self.posY