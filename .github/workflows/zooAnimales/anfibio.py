from zooAnimales.animal import Animal

class Anfibio(Animal):

    ranas = 0
    salamandras = 0
    _listado = []

    def __init__ (self, nombre = None, edad = 0, habitat = None, genero = None, colorPiel = None, venenoso = False):
        super().__init__(nombre, edad, habitat, genero)
        self._colorPiel = colorPiel
        self._venenoso = venenoso
        Anfibio._listado.append(self)

    @staticmethod
    def cantidadAnfibios():
        return len(Anfibio._listado)
    
    def movimiento():
        return "saltar"
    
    @classmethod
    def crearRana(cls, nombre, edad, genero):
        cls(nombre, edad, "selva", genero, "rojo", True)
        cls.ranas += 1

    @classmethod
    def crearSalamandra(cls, nombre, edad, genero):
        cls(nombre, edad, "selva", genero, "negro y amarillo", False)
        cls.salamandras += 1

    def isVenenoso(self):
        return self._venenoso
    
    def setVenenoso(self, venenoso):
        self._venenoso = venenoso

    def getColorPiel(self):
        return self._colorPiel
    
    def setColorPiel(self, colorPiel):
        self._colorPiel = colorPiel