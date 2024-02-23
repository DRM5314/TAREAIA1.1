import threading
import time


class View(threading.Thread):
    matriz = None

    def __init__(self,matriz):
        super().__init__()
        self.matriz = matriz

    def printFloor(self):
        for i in range(len(self.matriz)):
            for j in range(len(self.matriz[i])):
                print(self.matriz[i][j],end="")
            print("")
        print("\n")

    def setMatriz(self,matriz):
        self.matriz = matriz

    def run(self):
        while True:
            self.printFloor()
            time.sleep(1)