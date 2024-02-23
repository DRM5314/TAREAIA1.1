import threading
import math
import time
class RobotController(threading.Thread):
    robot = None
    room = None
    def __init__(self,robot,room):
        super().__init__()
        self.robot = robot
        self.room = room


    def cleanController(self):
        cleanX = self.room.getFloorX()
        cleanY = self.room.getFlootY()
        for i in range(cleanY):
            for j in range(cleanX):
                condition = self.room.areaFloor.getCondition(i,j)
                self.moveControler(i,j)
                condition = self.cleanControler(condition)
                self.robot.setMemory(condition)
        self.room.areaFloor.moveRobot(self.robot)
        if(self.room.areaFloor.getCondition(0,0)=="d"):
            self.room.areaFloor.dirtyArea(0,0)
        else:
            self.moveControler(0,0)
    def cleanControler(self,condition):
        return self.robot.scan(condition)
    def moveControler(self,posX,posY):
        self.room.areaFloor.moveRobot(self.robot)
        self.room.areaFloor.seeRobot(posX,posY,"R")
        self.robot.move(posX,posY)


    def cleanPos(self,posX,posY,radio):
        self.robot.move(posX,posY)
        area = math.pi*radio**2
        for i in range(360):
            percent = (i/360 * math.pi*radio**2) / area *100
            print(f"Proceso limpieza area: {percent:.2f}%")
            self.robot.clean()
        self.robot.move(posX,posY)

    def smartMove(self):
        posx = self.robot.getPosX()
        posy = self.robot.getPosY()
        maxX = self.room.getFloorWidth
        maxY = self.room.getFloorLength
        if(posx<maxX):
            if(posy<maxY):
                self.robot.move(posx,posy+1)
            else:
                self.robot.move(0,0)
        if(posy<maxY):
            if(posx<maxY):
                self.robot.move(posx+1,posy)
            else:
                self.robot.move(0,0)

    def run(self):
        while True:
            print("Iniciando ronda")
            self.cleanController()
            print("Descansando")
            time.sleep(10)
