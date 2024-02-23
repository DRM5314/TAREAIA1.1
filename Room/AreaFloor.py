class AreaFloor():
    matriz = []
    maxX = 0
    maxY = 0
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.maxX = x
        self.maxY = y
        self.matriz = [["-" for j in range(x)] for i in range(y)]


    def dirtyArea(self,posX,posY):
        if(posY <= self.maxX and posX <= self.maxY):
            self.matriz[posX][posY] = "d"
        else:
            print("Posicion no valida")

    def cleanArea(self,posX,posY):
        self.matriz[posX][posY] = "-"

    def seeRobot(self,posX,posY,name):
        if(name =="*R*"):
            print("Limpiando!")
        self.matriz[posX][posY] = name

    def moveRobot(self,robot):
        posX = robot.getPosX()
        posY = robot.getPosY()
        self.matriz[posX][posY] = robot.getMemory()

    def getCondition(self,posX,posY):
        return self.matriz[posX][posY]