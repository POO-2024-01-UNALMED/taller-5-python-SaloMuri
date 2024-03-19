class Zoologico:
  
  _zonas = []

  def __init__(self, nombre, ubicacion):
    self._nombre = nombre
    self._ubicacion = ubicacion   

  def agregarZonas(self, zona):
    self._zonas.append(zona)

  def cantidadTotalAnimales(self):
    cantidadTotal = 0
    for zona in self._zonas:
      cantidadTotal += zona.cantidadAnimales()
    return cantidadTotal
  
  def getNombre(self):
    return self._nombre

  def setNombre(self, nuevoNombre):
    self._nombre = nuevoNombre

  def getUbicacion(self):
    return self._ubicacion

  def setUbicacion(self, nuevaUbicacion):
    self._ubicacion = nuevaUbicacion
    
  @classmethod
  def getZona(cls):
    return cls._zonas
  
  @classmethod
  def setZona(cls, zonas):
    cls._zonas = zonas