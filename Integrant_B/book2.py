#declarem la classe amb les seves definicions
class book:
    # definim els atributs i fem el getter i el setter de cadascu
    def __init__(self, any, titol, autor, genere, ventes, tapa):
        self.any = any
        self.titol = titol
        self.autor = autor
        self.genere = genere
        self.ventes = ventes
        self.tapa = tapa

    def getAny(self):
        return self.any

    def setAny(self, any):
        self.any = any

    def getTitol(self):
        return self.titol

    def setTitol(self, titol):
        self.titol = titol

    def getAutor(self):
        return self.autor

    def setAutor(self, autor):
        self.autor = autor

    def getGenere(self):
        return self.genere

    def setGenere(self, genere):
        self.genere = genere

    def getVentes(self):
        return self.ventes

    def setVentes(self, ventes):
        self.ventes = ventes

    def getTapa(self):
        return self.tapa

    def setTapa(self, tapa):
        self.tapa = tapa

    def info(self):
        # fem el print de cada definicio
        print("L'any es: " + self.any)
        print("El titol es: " + self.titol)
        print("L'autor es: " + self.autor)
        print("El genere es: " + self.genere)
        print("Les ventes son: " + self.ventes)
        print("El tipus de tapa es: " + self.tapa)

    # Fem el metode per guardar els objectes en un diccionari
    def to_dict(self):
        return {
            "any": self.any,
            "titol": self.titol,
            "autor": self.autor,
            "genere": self.genere,
            "ventes": self.ventes,
            "tapa": self.tapa
        }
