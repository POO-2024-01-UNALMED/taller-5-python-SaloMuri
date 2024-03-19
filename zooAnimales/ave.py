from zooAnimales.animal import Animal

class Ave(Animal):
  _listado = []
  halcones = 0
  aguilas = 0

  def __init__(self, nombre, edad, habitat, genero, colorPlumas):
    super().__init__(nombre, edad, habitat, genero)
    self._colorPlumas = colorPlumas
    Ave._listado.append(self)

  def getColorPlumas(self):
    return self._colorPlumas

  def setColorPlumas(self, colorPlumas):
    self._colorPlumas = colorPlumas

  def movimiento():
    return "volar"
  
  @staticmethod
  def cantidadAves():
    return len(Ave._listado)

  @classmethod
  def crearHalcon(cls, nombre, edad, genero):
    Ave(nombre, edad, "montana", genero, "cafe glorioso")
    cls.halcones += 1

  @classmethod
  def crearAguila(cls, nombre, edad, genero):
    Ave(nombre, edad, "montana", genero, "blanco y amarillo")
    cls.aguilas += 1