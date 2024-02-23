
import time

from Room.Roomm import Room
from RobotClean.RobotClean import Robot
from RobotClean.Controller import RobotController
from Room.View import View
from Room.DirtyEntry import DirtyEntry

room = Room("piso 1",2,2)
robot = Robot("robot1")
controller = RobotController(robot,room)
view = View(room.areaFloor.matriz)
dirty = DirtyEntry(room.areaFloor)

controller.start()
view.start()
dirty.start()

