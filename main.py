import json
#importo els dos arxius Python de la carpeta A i la carpeta B
from Integrant_A.car import car
from Integrant_A.university2 import university
from Integrant_B.cat import cat
from Integrant_B.book2 import book
#faig les llistes de les dues clases i poso les dades de cada car i cada universitat
cars = [
    car("Peugeot", "406", "Vermell", "1998"),
    car("Ferrari", "812", "Negre", "2016"),
    car("Lamborghini", "Murcielago", "Groc", "2012"),
    car("Seat", "Ibiza", "Blanc", "2000"),
    car("Citroen", "C3", "Blau", "2022"),
]

universities = [
    university("Harvard","Espanya",500000,"Medicina",300,"No"),
    university("Cambridge","Italia",10,"Ingenieria",1000,"Si"),
    university("Universitat de Madrid", "Francia", 12932, "Matematiques", 30000, "Si"),
    university("UAB", "Alemanya", 10932, "Fisica", 10000, "Si"),
    university("Universitat Europea", "Libano", 100002, "Criminologia", 2500, "No"),
]


#convirteixo les dues llistes en diccionaris
cars_list = [c.to_dict() for c in cars]
universities_list = [u.to_dict() for u in universities]


#guardo les llistes en un objecte contenidor
data = {"cars":cars_list, "universities": universities_list}


#Guardo el contenidor en un arxiu .json
with open ("json_API/A.json", "w") as file:
    json.dump(data, file)


#Creem els objectes de les classes ficant-los a una llista
cats = [
    cat("4", "Curt", "Peix", "Mascle", "Entremeliat", "2"),
    cat("4", "Llarg", "Pinso", "Femella", "Timid", "6"),
    cat("3", "Curt", "Vedella", "Femella", "Salvatge", "8"),
    cat("4", "Curt", "Porc", "Femella", "Carinyos", "15"),
    cat("4", "Sense", "Pollastre", "Mascle", "Curios", "1"),
]

books = [
    book("1956","La Guerra","Marcos Aurelio","Historia","20000","Dura"),
    book("467","Alquimia Avanzada","San Fernando","Ciencia o Mito","400","Dura"),
    book("2012","El fin del mundo","Fran Mayas","Apocaliptico","500000","Blanda"),
    book("2021","La guerra contra les sustancies","Dr.Rallo","Economia","1000000","Dura"),
    book("50","La Biblia","Jesus","Historia","1000000000","Dura")
]


#Fiquem les llistes a dins d'un diccionari
cats_list = [c.to_dict() for c in cats]
books_list = [b.to_dict() for b in books]


#Fiquem els diccionaris a dins d'una altre llista
informacio = {"cats":cats_list,"books":books_list}


#I ho guardem a un .json
with open("json_API/b.json","w") as file:
    json.dump(informacio,file)