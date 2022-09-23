class Zona:
    def __init__(self, nombre, zoo=None):
        self.__nombre=nombre
        self.__zoo=zoo
        self.__animales=[]

    def agregarAnimales(self,animales):
        self.__animales.append(animales)

    def cantidadAnimales(self):
        return len(self.__animales) #mis dudas
    def setNombre(self,nombre):
        self.__nombre=nombre
    def getNombre(self):
        return self.__nombre
    def setZoo(self,zoo):
        self.__zoo.append(zoo)
    def getZoo(self):
        return self.__zoo
    def setAnimales(self, animales):
        self.__animales.append(animales)
    def getAnimales(self):
        self.__animales
    