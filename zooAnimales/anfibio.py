from zooAnimales.animal import  Animal

class Anfibio(Animal):
    ranas=0
    salamandras=0
    __listado=[]
    def __init__(self, nombre, edad, habitat, genero, colorPiel, venenoso):
        super().__init__(nombre, edad, habitat, genero)
        self.__colorPiel=colorPiel
        self.__venenoso=venenoso
    
    @classmethod
    def cantidadAnfibios(cls):
        return len(cls.__listado)

    def movimiento(self):
        return "saltar"

    @classmethod
    def crearRana(cls, nombre, edad, genero):
        rana= Anfibio(nombre, edad, "selva", genero, "rojo", True)
        cls.ranas +=1
        cls.__listado.append(rana)
        return rana
    
    @classmethod
    def crearSalamandra(cls, nombre, edad, genero):
        salamandra= Anfibio(nombre, edad, "selva", genero, "negro y amarillo", False)
        cls.__listado.append(salamandra)
        cls.salamandras +=1
        return salamandra
    
    def setColorPiel(self, colorPiel):
        self.__colorPiel=colorPiel
    def getColorPiel(self):
        return self.__colorPiel
    
    def setVenenoso(self, venenoso):
        self.__venenoso=venenoso
    def isVenenoso(self):
        return self.__venenoso
    
    @classmethod
    def setListado(cls, Anfibio):
        cls.__listado.append(Anfibio)
    @classmethod
    def getListado(cls):
        return cls.__listado