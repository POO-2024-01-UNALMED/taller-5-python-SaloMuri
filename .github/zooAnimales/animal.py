import zooAnimales

class Animal:

    _totalAnimales = 0
    
    def __init__ (self, nombre = None, edad = 0, habitat = None, genero = None, zona = None):
        self._nombre = nombre
        self._edad = edad
        self._habitat = habitat
        self._zona = zona
        self._genero = genero
        Animal._totalAnimales += 1

    def movimiento():
        return "desplazarse"
    
    @staticmethod
    def totalPorTipo(cls):
        return "Mamiferos: " + str(zooAnimales.mamifero.Mamifero.cantidadMamiferos()) + "\nAves: " + str(zooAnimales.ave.Ave.cantidadAves()) + "\nReptiles: " + str(zooAnimales.reptil.Reptil.cantidadReptiles()) + "\nPeces: " + str(zooAnimales.pez.Pez.cantidadPeces()) + "\nAnfibios: " + str(zooAnimales.anfibio.Anfibio.cantidadAnfibios())
    
    def toString(self):
        if self._zona != None:
            return "Mi nombre es " + str(self._nombre) + ", tengo una edad de " + str(self._edad) + ", habito en " + str(self._habitat) + " y mi genero es " + str(self._genero) + ", la zona en la que me ubico es " + str(self._zona.getNombre()) + ", en el zoo" + str(self._zona.getZoo().getNombre())
        else:
            return  "Mi nombre es " + str(self._nombre) + ", tengo una edad de " + str(self._edad) + ", habito en " + str(self._habitat) + " y mi genero es " + str(self._genero)
        
    def getNombre(self):
        return self._nombre
    
    def setNombre(self, nombre):
        self._nombre = nombre

    def getEdad(self):
        return self._edad
    
    def setEdad(self, edad):
        self._edad = edad

    def getHabitat(self):
        return self._habitat
    
    def setHabitat(self, habitat):
        self._habitat = habitat

    def getGenero(self):
        return self._genero
    
    def setGenero(self, genero):
        self._genero = genero

    @classmethod
    def getTotalAnimales(cls):
        return cls._totalAnimales
    
    @classmethod
    def setTotalAnimales(cls, totalAnimales):
        cls._totalAnimales = totalAnimales

    @classmethod
    def getZona(cls):
        return cls._zona
    
    @classmethod
    def setZona(cls, zona):
        cls._zona = zona