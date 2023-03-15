#declarem la classe amb les seves definicions
class university:
    #definim els atributs i fem el getter i el setter de cadascu
    def __init__(self, nom, ciutat, preu, carrera, alumnes, erasmus):
        self.nom = nom
        self.ciutat = ciutat
        self.preu = preu
        self.carrera = carrera
        self.alumnes = alumnes
        self.erasmus = erasmus

    def getNom(self):
        return self.nom

    def setNom(self, nom):
        self.nom = nom

    def getCiutat(self):
        return self.ciutat

    def setCiutat(self, ciutat):
        self.ciutat = ciutat

    def getPreu(self):
        return self.preu

    def setPreu(self, preu):
        self.preu = preu

    def getCarrera(self):
        return self.carrera

    def setCarrera(self, carrera):
        self.carrera = carrera

    def getAlumnes(self):
        return self.alumnes

    def setVentes(self, alumnes):
        self.alumnes = alumnes

    def getTapa(self):
        return self.erasmus

    def setTapa(self, erasmus):
        self.erasmus = erasmus

    def info(self):
        # fem el print de cada definicio
        print("El nom es: " + self.nom)
        print("Está a la ciutat de: " + self.ciutat)
        print("La matricula costa: " + self.preu)
        print("La carrera es: " + self.carrera)
        print("N'hi han : " + self.alumnes + "alumnes")
        print("El pais d'erasmus es" + self.erasmus)

    def to_dict(self):
        # Converteixo l'objecte en un format json
        return {
            "nom": self.nom,
            "ciutat": self.ciutat,
            "matricula": self.preu,
            "carrera": self.carrera,
            "alumnes": self.alumnes,
            "erasmus": self.erasmus
        }
