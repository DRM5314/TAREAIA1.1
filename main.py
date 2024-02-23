
import time

from Room.Roomm import Room
from RobotClean.RobotClean import Robot
from RobotClean.Controller import RobotController
from Room.View import View
from Room.DirtyEntry import DirtyEntry

print("Acciones:  \n\tR -> Robot     *R* -> Robot limpiando   d -> Area sucia (Dirty)   - -> Cuadrante")
print("Mensajes:  \n\tArea limpia     Area sucia       Limpiando    Limpio!")
print("Acciones:  \n\ti -> ingresar nueva area      seguido digito,digito     s -> Robot smart   e -> Robot estupido")
time.sleep(20)


room = Room("piso 1",2,1)
robot = Robot("robot1")
controller = RobotController(robot,room)
view = View(room.areaFloor.matriz)
dirty = DirtyEntry(room.areaFloor,robot)

controller.start()
view.start()
dirty.start()

