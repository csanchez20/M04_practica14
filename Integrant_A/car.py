#declarem la classe amb les seves definicions
class car:
    # definim els atributs i fem el getter i el setter de cadascu
    def __init__(self, marca, model, color, any):
        self.marca = marca
        self.model = model
        self.color = color
        self.any = any

    def getMarca(self):
        return self.marca

    def setMarca(self, marca):
        self.marca = marca

    def getModel(self):
        return self.model

    def setModel(self, model):
        self.model = model

    def getColor(self):
        return self.color

    def setColor(self, color):
        self.color = color

    def getAny(self):
        return self.any

    def setAny(self, any):
        self.any = any

    def cars(self):
        # fem el print de cada definicio
        print("La marca del cotxe es: " + self.marca)
        print("El model del cotxe es: " + self.model)
        print("El color del cotxe es: " + self.color)
        print("Es va fabricar a l'any: " + self.any)

    #Converteixo l'objecte en un format json
    def to_dict(self):
        return {
            "marca": self.marca,
            "model": self.model,
            "color": self.color,
            "any": self.any
        }
