class Zoologico:
  
  _zonas = []

  def __init__(self, nombre, ubicacion):
    self._nombre = nombre
    self._ubicacion = ubicacion   

  def agregarZonas(self, zona):
    self._zonas.append(zona)

  def cantidadTotalAnimales(self):
    cantidadA = 0
    for zona in self._zonas:
      cantidadA += zona.cantidadAnimales()
    return cantidadA
  
  def getNombre(self):
    return self._nombre

  def setNombre(self, nNombre):
    self._nombre = nNombre

  def getUbicacion(self):
    return self._ubicacion

  def setUbicacion(self, nUbicacion):
    self._ubicacion = nUbicacion
    
  @classmethod
  def getZona(cls):
    return cls._zonas
  
  @classmethod
  def setZona(cls, zonas):
    cls._zonas = zonas