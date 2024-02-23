import threading
import keyboard
class DirtyEntry(threading.Thread):
    areaFloor = None
    robot = None
    def __init__(self,areaFloor,robot):
        super().__init__()
        self.areaFloor = areaFloor
        self.robot = robot

    def run(self):
        while True:
            a = keyboard.read_key()
            if a == "i":
                newPos = input("Ingrese nueva posicion para basura: ")
                positions = newPos.split(",")
                self.areaFloor.dirtyArea(int(positions[1]),int(positions[0]))
            elif a == "e":
                print("Cambiando a estupida")
                self.robot.setSmart(False)
            elif a == "s":
                print("Cambiando a smart")
                self.robot.setSmart(True)