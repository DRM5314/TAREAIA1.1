from TestImport.Hijo import Hijo
class Padre:
    adn = 123
    hijo = None
    def __init__(self):
        self.hijo = Hijo(self)

    def getAdnPadre(self):
        return self.adn
