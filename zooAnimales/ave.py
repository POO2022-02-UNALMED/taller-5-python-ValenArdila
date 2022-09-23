from zooAnimales.animal import Animal
class Ave(Animal):
    halcones=0
    aguilas=0
    __listado=[]
    def __init__(self, nombre, edad, habitat, genero, colorPlumas):
        super().__init__(nombre, edad, habitat, genero)
        self.__colorPlumas=colorPlumas
        

    
    @classmethod
    def cantidadAves(cls):
        return len(cls.__listado)
    
    def movimmiento(self):
        return "volar"
    
    @classmethod
    def crearHalcon(cls, nombre, edad, genero):
        halcon= Ave(nombre, edad, "montanas", genero, "cafe glorioso")
        cls.halcones +=1
        cls.__listado.append(halcon)
        return halcon
    
    @classmethod
    def crearAguila(cls, nombre, edad, genero):
        aguila= Ave(nombre, edad, "montanas", genero, "blanco y amarillo")
        cls.__listado.append(aguila)
        cls.aguilas +=1
        return aguila
    
    def setColorPlumas(self, colorPlumas):
        self.__colorPlumas=colorPlumas
    def getColorPlumas(self):
        return self.__colorPlumas
    
    @classmethod
    def setListado(cls, Ave):
        cls.__listado.apppend(Ave)
    def getListado(cls):
        return cls.__listado