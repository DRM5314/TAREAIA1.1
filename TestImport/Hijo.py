class Hijo:
    padre = None

    def __init__(self,padre):
        self.padre = padre

    def getAdnHijo(self):
        return self.padre.getAdnPadre()+2