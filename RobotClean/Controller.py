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


    def cleanController(self,all):
        cleanX = self.room.getFloorX()
        cleanY = self.room.getFlootY()
        size = cleanX*cleanY
        accumulatedY = 0
        accumulatedX = 0
        for i in range(cleanX):
            for j in range(cleanY):
                condition = self.room.areaFloor.getCondition(i,j)
                self.moveControler(i, j)
                if(all):
                    self.robot.clean()
                    self.room.areaFloor.cleanArea(i,j)
                else:
                    ne = self.robot.scan(condition)
                    if ne == "d":
                        self.room.areaFloor.cleanArea(i, j)

    def moveControler(self,posX,posY):
        afterX = self.robot.getPosX()
        afterY = self.robot.getPosY()
        self.room.areaFloor.moveRobot(afterX,afterY)
        self.room.areaFloor.seeRobot(posX,posY)
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
            self.cleanController(True)
            time.sleep(5)
            self.cleanController(False)
            time.sleep(10)