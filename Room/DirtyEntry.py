import threading
import keyboard
class DirtyEntry(threading.Thread):
    areaFloor = None
    def __init__(self,areaFloor):
        super().__init__()
        self.areaFloor = areaFloor

    def run(self):
        a = keyboard.read_key()
        while a == "i":
            newPos = input("Ingrese nueva posicion para basura: ")
            positions = newPos.split(",")
            self.areaFloor.dirtyArea(int(positions[0]),int(positions[1]))
