from zooAnimales.animal import Animal

class Ave(Animal):

    halcones = 0
    aguilas = 0
    _listado = []

    def __init__ (self, nombre, edad, habitat, genero, colorPlumas):
        super().__init__ (nombre, edad, habitat, genero)
        self._colorPlumas = colorPlumas
        Ave._listado.append(self)

    @staticmethod
    def cantidadAves():
        return len(Ave._listado)
    
    def movimiento():
        return "volar"
    
    @classmethod
    def crearHalcon(cls, nombre, edad, genero):
        Ave(nombre, edad, "montana", genero, "cafe glorioso")
        cls.halcones += 1
    
    @classmethod
    def crearAguila(cls, nombre, edad, genero):
        Ave(nombre, edad, "montana", genero, "blanco y amarillo")
        cls.aguilas += 1

    def getColorPlumas(self):
        return self._colorPlumas
    
    def setColorPlumas(self, colorPlumas):
        self._colorPlumas = colorPlumas