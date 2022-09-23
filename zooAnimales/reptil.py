from zooAnimales.animal import Animal
class Reptil(Animal):
    iguanas=0
    serpientes=0
    __listado=[]
    def __init__(self, nombre, edad, habitat, genero, colorEscamas, largoCola):
        super().__init__(nombre, edad, habitat, genero)
        self.__colorEscamas=colorEscamas
        self.__largoCola=largoCola
        

    
    @classmethod
    def cantidadReptiles(cls):
        return len(cls.__listado)

    def movimiento(self):
        return "reptar"
    
    @classmethod
    def crearSerpiente(cls, nombre, edad, genero):
        serpiente= Reptil(nombre, edad, "jungla", genero, "blanco", 1)
        cls.serpientes +=1
        cls.__listado.append(serpiente)
        return serpiente
    
    @classmethod
    def crearIguana(cls, nombre, edad, genero):
        iguana= Reptil(nombre, edad, "humedal", genero, "verde", 3)
        cls.__listado.append(iguana)
        cls.iguanas +=1
        return iguana

    def setColorEscamas(self,colorEscamas):
        self.__colorEscamas=colorEscamas
    def getColorEscamas(self):
        return self.__colorEscamas

    def setLargoCola(self,largoCola):
        self.__largoCola=largoCola
    def getLargoCola(self):
        return self.__largoCola
    
    @classmethod
    def getListado(cls):
        return cls.__listado
    @classmethod
    def setListado(cls, Reptil):
        cls.__listado.append(Reptil)