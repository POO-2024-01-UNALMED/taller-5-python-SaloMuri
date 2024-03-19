from zooAnimales.animal import Animal

class Reptil(Animal):

    iguanas = 0
    serpientes = 0
    _listado = []

    def __init__ (self, nombre = None, edad = 0, habitat = None, genero = None, colorEscamas = None, largoCola = False):
        super().__init__(nombre, edad, habitat, genero)
        self._colorEscamas = colorEscamas
        self._largoCola = largoCola
        Reptil._listado.append(self)

    @staticmethod
    def cantidadReptiles():
        return len(Reptil._listado)
    
    def movimiento():
        return "reptar"
    
    @classmethod
    def crearIguana(cls, nombre, edad, genero):
        Reptil(nombre, edad, "humedal", genero, "verde", 3)
        cls.iguanas += 1
    
    @classmethod
    def crearSerpiente(cls, nombre, edad, genero):
        Reptil(nombre, edad, "jungla", genero, "blanco", 3)
        cls.serpientes += 1

    def getColorEscamas(self):
        return self._colorEscamas
    
    def setColorEscamas(self, colorEscamas):
        self._colorEscamas = colorEscamas

    def getLargoCola(self):
        return self._largoCola
    
    def setLargoCola(self, largoCola):
        self._largoCola = largoCola