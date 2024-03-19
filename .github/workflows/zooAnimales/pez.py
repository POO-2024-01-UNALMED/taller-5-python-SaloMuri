from zooAnimales.animal import Animal
class Pez(Animal):

    salmones = 0
    bacalaos = 0
    _listado = []

    def __init__ (self, nombre = None, edad = 0, habitat = None, genero = None, colorEscamas = None, cantidadAletas = 0):
        super().__init__(nombre, edad, habitat, genero)
        self._colorEscamas = colorEscamas
        self._cantidadAletas = cantidadAletas
        Pez._listado.append(self)

    @staticmethod
    def cantidadPeces():
        return len(Pez._listado)
    
    def movimiento():
        return "nadar"
    
    @classmethod
    def crearSalmon(cls, nombre, edad, genero):
        Pez(nombre, edad, "oceano", genero, "rojo", 6)
        cls.salmones += 1
    
    @classmethod
    def crearBacalao(cls, nombre, edad, genero):
        Pez(nombre, edad, "oceano", genero, "gris", 6)

    def getColorEscamas(self):
        return self._colorEscamas
    
    def setColorEscamas(self, colorEscamas):
        self._colorEscamas = colorEscamas

    def getCantidadAletas(self):
        return self._cantidadAletas
    
    def setCantidadAletas(self, cantidadAletas):
        self._cantidadAletas = cantidadAletas
    