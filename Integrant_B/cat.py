#declarem la classe amb les seves definicions
class cat:
    # definim els atributs i fem el getter i el setter de cadascu
    def __init__(self,potes,pel,menjarPreferit,sexe,personalitat,anys):
        self.potes = potes
        self.pel = pel
        self.menjarPreferit = menjarPreferit
        self.sexe = sexe
        self.personalitat = personalitat
        self.anys = anys

    def getPotes(self):
        return self.potes
    def setPotes(self,potes):
        self.potes = potes
    def getPel(self):
        return self.pel
    def setPel(self,pel):
        self.pel = pel
    def getMenjarPreferit(self):
        return self.menjarPreferit
    def setMenjarPreferit(self,menjarPreferit):
        self.menjarPreferit = menjarPreferit
    def getSexe(self):
        return self.sexe
    def setSexe(self,sexe):
        self.sexe = sexe
    def getPersonalitat(self):
        return self.personalitat
    def setPersonalitat(self,personalitat):
        self.personalitat = personalitat
    def getAnys(self):
        return self.anys
    def setAnys(self,anys):
        self.anys = anys

    # fem el print de cada definicio
    def info(self):
        print("Potes: " + self.potes)
        print("Pel: " + self.pel)
        print("Menjar Preferit: " + self.menjarPreferit)
        print("Sexe: " + self.sexe)
        print("Personalitat: " + self.personalitat)
        print("Anys: " + self.anys)


    #Fem el metode per guardar els objectes en una diccionari
    def to_dict(self):
        return {
            "potes": self.potes,
            "pel": self.pel,
            "menjarPreferit": self.menjarPreferit,
            "sexe": self.sexe,
            "personalitat": self.personalitat,
            "anys": self.anys
        }
