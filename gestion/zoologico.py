class Zoologico:
    __zonas=[]
    def __init__(self, nombre, ubicacion):
        self.__nombre=nombre
        self.__ubicacion=ubicacion
        
    
    def agregarZonas(self,zonas):
        self.__zonas.append(zonas)
    def cantidadTotalAnimales(self):
        suma = 0
        i = 0
        while i < len(self.__zonas):
            suma += self.__zonas[i].cantidadAnimales()
            i += 1
        return suma
    def setNombre(self, nombre):
        self.__nombre=nombre
    def getNombre(self):
        return self.__nombre
    def setUbicacion(self, ubicacion):
        self.__ubicacion=ubicacion
    def getUbiacion(self):
        return self.__ubicacion
    def setZonas(self, zonas):
        self.__zonas.append(zonas)
    def getZona(self):
        return self.__zonas
