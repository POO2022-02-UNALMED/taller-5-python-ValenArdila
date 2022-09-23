from zooAnimales.animal import Animal

class Pez(Animal):
    salmones=0
    bacalaos=0
    __listado=[]
    def __init__(self, nombre, edad, habitat, genero, colorEscamas, cantidadAletas):
        super().__init__(nombre, edad, habitat, genero)
        self.__colorEscamas=colorEscamas
        self.__cantidadAletas=cantidadAletas
        

    
    
    @classmethod
    def cantidadPeces(cls):
        return len(cls.__listado)
    
    def movimientp(self):
        return "nadar"
    
    @classmethod
    def crearSalmon(cls, nombre, edad, genero):
        salmon= Pez(nombre, edad, "oceano", genero, "rojo", 6)
        cls.salmones +=1
        cls.__listado.append(salmon)
        return salmon
    
    @classmethod
    def crearBacalao(cls, nombre, edad, genero):
        bacalao= Pez(nombre, edad, "oceano", genero, "gris", 6)
        cls.__listado.append(bacalao)
        cls.bacalaos +=1
        return bacalao
    
    @classmethod
    def setListado(cls, Pez):
        cls.__listado.append(Pez)
    @classmethod
    def getListado(cls):
        return cls.__listado

    def setColorEscamas(self, colorEscamas):
        self.__colorEscamas=colorEscamas
    def getColorEscamas(self):
        return self.__colorEscamas
    
    def setCantidadAletas(self, cantidadAletas):
        self.__cantidadAletas=cantidadAletas
    def getCantidadAletas(self):
        return self.__cantidadAletas