from Room.AreaFloor import AreaFloor
class Room:
    name = "RoomDefault"
    x = 10
    y = 10
    noFloors = 2
    areaFloor = None

    def __init__(self,name,x,y):
        self.areaFloor = AreaFloor(x,y)
        self.name = name
        self.x = x
        self.y = y
    def getFloorX(self):
        return self.x

    def getFlootY(self):
        return self.y

    def getAreaFloor(self):
        return self.areaFloor